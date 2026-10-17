# Bounded floating active-branch scout
2026-10-17. Prepared for Edward Baker; gpt-6.1-sol (Codex), inherited ultra effort; same-model diagnostic, no certificate.

Scope fixed before evaluation: t=0.157, y in [sqrt(.0350708),sqrt(.686)], N and Euler P equal (690988,[2,3,5,7,11]), (728999,[2,3,5,7,11]), (729000,[2,3,5,7]), (818999,[2,3,5,7]), (819000,[2,3,5]), (1027999,[2,3,5]), (1028000,[2,3]), (3840000,[2,3]). This is selected starts/seams/tail endpoint, not coverage of all N.

For each G|D enumerate feasible active-divisor patterns by consecutive divisor thresholds dN. Select actual integers n=Gk with gcd(k,D/G)=1 at interval endpoints, five equally spaced log positions, and near any C0(L) sign roots found on a 33-point log grid and bisected 60 times. Keep only actual n and deduplicate. Evaluate 25 equally spaced y nodes including both ends. Hard limits: <=200000 actual term-y evaluations; wall time <=120 seconds, measured in the program; abort with explicit incomplete marker on either limit. No full finite-row sum or row sweep. Store worst positive and least-negative active gate values and at most 20 witnesses.

Normalize by b_t(n)>0. Compute both active branches, retaining numerical ties, Eq.(2) with sigma'=1/2, and actual frozen-sigma derivative. Also record true weighted derivative including n^-sigma and b_t(n). Floating arithmetic only, no numerical sign becomes a certificate. Any likely obstruction must be replayed outward by the parent.
