# MC03-E01: separate check of the complete Mellin response

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Reviewer **gpt-6.1-sol (Codex), reasoning effort ultra**, verified in reviewer session 01a19a54-ed89-7c00-8f73-efd0c7a7a8db, turn 01a19a54-ed9e-7702-9cd0-35e66e2e20db, agent /root/review_response_oscillator. The assessed authoring return records **gpt-6-astra / ultra**, session 01a19a49-d2ca-7ab1-b502-4e2795ee4f33, turn 01a19a49-d2e8-7940-8e28-d3ab8a4b9600; those fields match its actual authoring metadata.

**Disposition: accept the fixed claims at their stated scope; no mathematical correction identified. MC03-E01 r1 is complete.** The full-source fixed-box local limit, its nonzero normalization, the exact centered response and the conditional comparison are valid. The complete theta Mellin inequality remains unresolved on every claimed global domain. In particular, the conditional number \(S_0=4\pi e^8\) is not a theta tail threshold.

This is separate cross-model internal checking with the shared repository baseline. It does not independently reprove the accepted source-sign certificate and is not independent specialist review. Only this review is owned here; the return, support files, registers, catalogs and shared history were not edited.

## Fixed inputs and evidence

The [request r1](../numerics/MC03_E01_REVIEW_REQUEST_R1_20261101.json), [frozen return](../notes/01_COMPLETE_MELLIN_RESPONSE_RETURN_20261101.md), [exact support checker](../numerics/mc03_exact_gaussian_check.py) and [saved support record](../numerics/MC03_B01_EXACT_RECORD_20261101.json) were read and hashed before acceptance.

| Input | Verified SHA-256 |
| --- | --- |
| Request r1 | 66f4b0a1818acfb3fe034c5d312e04f368a964b025a1f20806f1dd97ab663252 |
| Frozen return; matches request | 8d2727fbdde5c87673ecf61a1efba40b9072f2108ed299c6b162d3cf19235183 |
| Exact Gaussian checker; matches record | 019659d69d0e6c8a4df22aa984234fa443036a20be473902f1e8d285285e1dbd |
| Saved Gaussian record | 06460ae1423e719c667c110f157a1aacc6255d37a4a8ad20bae4c7b14e1b9732 |
| Initial Mellin assessment | ee4280708b43d4d080fe98c128d58c0180f0ba0851b730bd859c2a899f84d9de |
| Parent Note03 | 0d6167397219a4dd11dbb5650c5c3c5d31a8e17d7a22a6b81eba81af50fb091f |
| Parent Note04 | f4ff6338794cf359bf06ea6ec17867fd5aef44910de1796b3c26396f8fb5b720 |
| Continuation05 | 7cfa21664fe85e64749a7fc4e32c420300b8d91590f0dc62da35cf3816e677d7 |
| Launch record | 501acdcfa663b5eb4959c348095a4e79c70053907660b599f3585862a526f60a |
| J-E01 r2 complete-source differentiated tail | 202a37845f602efd56c8d11935cb8256c665edbaaae421b1b2fed14c186e97d2 |
| Accepted J-E03 Review01 | c13e63e7c017285932e75d2add333b8d683e5ed3b9a096f6e20e31e88e0a2dfe |

The [result summaries](../../../../../../../result-summaries/README.md), especially [theta bookkeeping](../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md) and [collision controls](../../../../../../../result-summaries/12_collision_controls_and_screening.md), and the [patterns to avoid](../../../../../../../avoid/README.md), especially [shared premises](../../../../../../../avoid/05_same_model_reviews_and_shared_premises.md), [normalization](../../../../../../../avoid/08_normalization_and_constant_slips.md) and [joint signed estimates](../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md), govern the status.

## Analytical checks

**Saddle and full-source local density: accept.** For \(F_s(u)=2s\log u-\pi e^{4u}\), the equation \(s=2at\), \(t=\pi e^{4a}\), gives \(F_s'(a)=0\) and
\[
-F_s''(a)=\frac{2s(1+4a)}{a^2}=\sigma^{-2}.
\]
The equation has one positive solution; \(a\to\infty\), \(\sigma\to0\). On a fixed \(x\)-box the cubic Taylor remainder is \(O_L(\sigma)\). The complete differentiated theta remainder in J-E01 r2 gives the required uniform first-mode approximation on that moving box. The prefactor is \(2e^at^2\); the omitted \(e^{9\sigma x}\) and \(1-3/(2\pi e^{4u})\) tend uniformly to one.

The inherited jet formulas give \(R'\sim128t^2\) and \(g''\to2\). The simplex formula has area \(1/2\), hence \(h_3\to1\). For a pair \(x_i,x_j\), divide \(R(a+\sigma x_j)-R(a+\sigma x_i)\) by \(\sigma(x_j-x_i)\) using its mean-value integral. This remains continuous at equality and converges uniformly to \(128t^2\). The same calculation for \(u_j^2-u_i^2\) yields \(2a\sigma(x_j-x_i)\). Therefore the two Vandermondes contribute six powers of \(\sigma\), the volume three, and
\[
K(s)=(2e^at^2)^3e^{3F_s(a)}(256at^2)^3\sigma^9
\]
is correct. The ratio of the rescaled density to \(e^{-\sum x_j^2/2}V(x)^2\) extends across every collision face and converges uniformly to one on each fixed ordered box. No separated-node hypothesis is needed.

This is a local limit of the complete signed source. It gives no domination on the expanding chamber and does not discard the negative origin insertion. The Gaussian Hermitian-matrix terminology and ordered normalization agree with [Tao, Notes 6, Section 1, equation (1)](https://terrytao.wordpress.com/2010/02/23/254a-notes-6-gaussian-ensembles/), inspected for this convention only. No random-matrix universality theorem is used.

**Exact centered response: accept.** Absolute integrability with two logarithmic insertions gives \(M^{(p)}=\int T^pf_s\), \(p=0,1,2\), including \(s=0\). The inherited real-tilt argument gives \(M(s)>0\). At an evaluation point, replacing \(T\) by \(T-6\log a(s)\) changes neither centered algebraic expression; it is not differentiation of a moving observable. With the return's exact \(Y_s\) and \(I_p\),
\[
\mathcal C_3(s)=\left(\frac{2\sigma}{a}\right)^2
\left[\frac{I_2}{I_0}-\left(\frac{I_1}{I_0}\right)^2\right]
=\frac{2}{s(1+4a)}
\left[\frac{I_2}{I_0}-\left(\frac{I_1}{I_0}\right)^2\right].
\]
This uses all signed integrals and no differentiated asymptotic error. The original formula includes \(s=0\); these rescaled coordinates require \(s>0\).

**Conditional budgets: accept, with their explicit conditional scope.** From \(I_0\ge1/2\), \(I_2\le6\), the real square gives \(\mathcal C_3\le24/[s(1+4a)]\). This argument does not require \(I_2\ge0\). At \(s\ge4\pi e^8\), \(a\ge2\), and
\[
\frac{24}{s(1+4a)}\le\frac{24}{9s}
\le\frac3{s+5/2}\le\kappa_3(s);
\]
the middle inequality is precisely \(s\ge20\). The decreasing-series integral bound proves the last inequality. The chosen budgets have not been established for theta.

The four split inequalities \(A_0\ge3/4,A_2\le4,B_0\ge-1/4,B_2\le2\) imply those two budgets. The fixed-box limit establishes only the first pair eventually, without an effective threshold. The mixed/off-saddle \(B_0,B_2\) payments remain open.

## Fixed replay, domains and disposition

One read-only replay of the unchanged checker passed, and every returned field matches the saved record. Exact rational Gaussian algebra gives normalization 12 relative to three independent normals, then \(E_GX=0,E_GX^2=3,E_GQ=9,E_G(X^2Q)=33\). Division by \(3!\) yields the ordered integral \(G=2(2\pi)^{3/2}\). At \(L=12\), the outside mass and \(X^2\)-moment bounds are \(9/144=1/16\) and \(33/144=11/48\). Since the limiting box mass is at least \(15/16\) and its second trace moment at most 3, the claimed eventual local budgets follow. The script does not evaluate theta or prove localization.

The undivided determinant pays origin and collision regularity; double-exponential tails pay fixed logarithmic insertions for compact \(s\) ranges. They do not pay estimates relative to the shrinking saddle normalization on the expanding chamber. All of \([0,2]\), any remaining compact Mellin interval and an effective unbounded theta tail remain unpaid. The Gaussian-source equality \(\mathcal C_3=\kappa_3\) is an independent exact normalization check, distinct from the local GUE model.

The two-point relaxation still defeats association-only inference and lacks the canonical source realization. Euler-factor and altered square-source controls fail unchanged canonical arithmetic data; reflected super-Gaussian controls fail the specific saddle tail. Their quantitative signed allowances were not tested. Some altered sources can share a local saddle model; that model alone does not screen them or prove theta signs. Positive-time collisions do not contradict this time-zero order-three statement.

**Accepted:** the local full-source theorem through collision faces, exact centered-score identity, Gaussian constants and conditional budget implication. **Corrections:** none. **Unresolved fixed-review defects:** none identified. **Unresolved research obligation:** prove the complete signed allowances with an explicit common threshold, then address the compact complement. The physical local model is a useful structural result; no Mellin sign estimate, new coefficient range or RH conclusion follows from this review. The already declared MC03-B02 remains a B/Astra localization task; this review authorizes no numerical campaign.
