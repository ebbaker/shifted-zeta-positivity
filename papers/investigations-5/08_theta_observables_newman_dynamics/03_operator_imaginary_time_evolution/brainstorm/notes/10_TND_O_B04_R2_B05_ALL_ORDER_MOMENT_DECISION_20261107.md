# B04 r2 / B05 r1: all-order endpoint moments and the one-pair cost

6 November 2026 America/New_York (7 November UTC). Prepared for **Edward Baker** with substantial OpenAI Codex assistance. Lead tool-selected configuration: **gpt-6-astra, ultra**; no independent backend verification.

**Decision:** after obtaining a paid local transport modulus, a collision consumer still needs independently small endpoint mass or signed flux. Compare two actual acquisition mechanisms. Select one bounded canonical time-zero moment corollary with explicit constants for every integer order, then test it against a single pair. This is E10 r2 with its B05 statistical consumer included; E11 need not duplicate the same scalar comparison.

| Candidate | Exact quantitative issue | Decision |
| --- | --- | --- |
| Invert fixed-offset one-body resolvent bounds | Replacing a real double root at X by X±id changes its logarithmic derivative by −2d²/[u(u²+d²)], u=z−X, only O(d²) on a fixed safe line. An O(1) remainder does not force d=O(R) as R→0. A raw harmonic linear kernel nonnegative across a strip and zero on its real axis is identically zero; subtraction of an unknown projected real-zero baseline is additional information. | The inspected coarse bounds do not pay a positive transverse mass estimate. This excludes only inference from those retained error allowances, not exact canonical inversion or nonlinear/coupled estimates. |
| Global canonical zero density plus the local count | Layer-cake integration of the exponential transverse tail and a deterministic local count give a moment bound whose p-dependence can be tracked explicitly | Select an all-p proof and optimization. It is a quantitative corollary of the imported density theorem, with no priority claim. |

## Fixed proposed theorem and proof route

Use H coordinates z=x+iy and H0=xi(1/2+iz/2)/8, so x=2t and |y|=2|beta−1/2|. Let 0<=chi<=1, chi supported in [-1,1], with a nontrivial unit plateau for the one-pair test. For T>=T0, 0<R<=1 and X in [T,2T], define

    Q_X=sum_j chi((x_j-X)/R) y_j²,  L=log T.

The target is absolute constants A>=1 and C>=1 depending only on chi and one fixed density exponent, such that **simultaneously for every integer p>=1**,

    (1/T) integral_T^(2T) Q_X^p dX <= C R A^p (2p)! / L^p.             (M)

No RH, simplicity or growing-order implicit constants. Complete multiplicities and the entire zero set are retained. At fixed p this is a local-average theorem; at p=p(T) it is still valid with the displayed factorial.

The imported inputs are Maples–Rodgers, arXiv:1404.3080v2, Corollary2.3 and Theorem2.4 (equivalently the exponential tail in §4 Eq(18)). For a fixed c in (0,1), the density constant depends on c but not on sigma in the relevant half-strip. Reflection doubles the right-half count. Thus, for the required dyadic H band and 0<v<=1,

    #{j: x_j in [T−R,2T+R], |y_j|>v} <= C0 T L exp(−a v L),

with a>0 fixed. The factor-of-two in y and the H/zeta height coordinates must be paid explicitly. The local count is <=C1 L. Then

    Q_X^p <=(C1 L)^(p−1) sum_j chi((x_j−X)/R)|y_j|^(2p).

Integrate X, paying each root's center width <=R||chi||_1. Layer cake with the displayed density tail gives the Gamma integral (2p)!/(aL)^(2p), proving (M). This uses monotone power tests directly; no claim for arbitrary spiky positive tests is imported.

## B05 consumer and acceptance test

A conjugate off-line H0 pair x0±id, 0<d<1, away from the center-band edges contributes Q_X>=2d² on a center interval of length comparable to R. Its p-th averaged signal is >=c_chi (R/T)(2d²)^p. Compare the explicit upper allowance (M) with that signal for **every** p, allowing p to grow arbitrarily with T.

The useful expected conclusion is a scoped failure of this paid estimate: factorial growth makes its best normalized allowance subpolynomial rather than T^-1. One elementary route is e^B>=B^(2p)/(2p)!, giving (2p)!/B^(2p)>=e^-B for B=sqrt(2d² L/A). Consequently the ratio of the available upper allowance to the one-pair lower signal is >=constant*T*exp(−O(sqrt L)), and tends to infinity uniformly over integer p. If this reasoning needs a constant/normalization repair, E10 r2 may make it explicitly. It must distinguish a lower bound on the **chosen upper allowance** from a lower bound on the actual moment or exceptional probability.

This is stronger order control than repeating the inherited fixed-k insufficiency: it supplies one genuine canonical all-order inequality and an all-order optimization obstruction for that inequality. It does not say all moment methods fail; sharper local density, prime correlations, coupled cancellation or a different observable lie outside the statement. It also does not provide full-path collision coverage. The inherited tube is not silently assumed to reach time zero.

## Bounded scope and continuation

E10 r2 owns one exact theorem/consumer package and one local correction. It is independent of E10 r1's simple-root transport proof, since it concerns only the canonical zero slice and the fixed published density input; a disjoint worker may prove it concurrently. E12 will assemble the transport estimate across collisions separately. An eventual E13 assessment should check both source uniformity and the distinction between actual moments and allowances. A failed one-pair comparison is the completed bounded result, not a request for more moment orders.

Mandatory [result index](../../../../../../result-summaries/README.md), [control cluster](../../../../../../result-summaries/12_collision_controls_and_screening.md), [patterns index](../../../../../../avoid/README.md), [classification](../../../../../../avoid/01_restating_the_target.md) and [scope discipline](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md) apply. Polynomial sharpness controls are not claimed to satisfy the canonical global density theorem. The failure here follows from the exact allowance itself, so no false arithmetic control premise is needed. The missing step after (M) is an independently stronger canonical endpoint/flux estimate that beats the one-pair center cost; merely renaming it is not a new task.
