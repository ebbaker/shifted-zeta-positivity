# VCD-E06 r1 — fixed-polynomial loss and exponential score reference

16 November 2026, America/New_York. Prepared for Edward Baker with OpenAI Codex assistance. Type E, parent B02 decision04. Lead backend/effort unavailable; helper explicitly gpt-6.1-sol/ultra. One fixed analytical theorem bundle, one correction pass, no numerical scan. Read root instructions, result/avoid indexes and E05. Exact source/readout unchanged, uniform lambda in [0,1/2].

## Frozen claims and route

1. For a fixed odd polynomial p of degree d, use finite Jacobi paths and the inherited envelope to give an explicit bound |a_n[p(J)]_(n,n-1)| <= A_(n,d) sum_k |p_k| (2A_(n,d))^k with a justified local coefficient majorant A. Conclude a_n<q_n,(V'-p)q_(n-1)> = n + O_p(log^(d+1)(n+2)), uniformly lambda. Therefore a fixed p with negligible relative remainder is impossible at large degree. State that n-dependent degrees/coefficients are not excluded.

2. Derive V_lambda'(u)=8πsinh(4u)-2lambda*u+b(u), where b is odd, time-independent and bounded for actual theta. Use positive mode scores, r_m=m²ρ, ρ=πexp(4u), s_m/s_1 <= 2m^4 exp(-(m²-1)ρ). A permissible explicit bound is 9+12/(2π-3)+4π+8π sum_(m>=2) m^4(m²-1)exp(-π(m²-1)); justify convergence, no decimal certification needed. Check factors and endpoints. Obtain |8π a_n[sinh(4J)]_(n,n-1)-2lambda beta_n-n| <= ||b||infinity*a_n. Give absolute and relative rates with the existing envelope. Define all matrix elements by multiplication on polynomial vectors and justify integrability/series uses.

3. Give exact one-site boundary decomposition for this exponential reference if available by applying already audited Duhamel/functional calculus, but do not claim a closed invariant. At minimum state precisely why this estimate carries no sign of the Fourier observation. E07 supplies actual controls sharing asymptotically small canonical-score residuals. This theorem changes retained information from fixed polynomial to an exponential score plus bounded exact b; it does not endorse dropping b in a zero proof.

Completion: written proofs or exact corrected claims, cost of remainder, scoped disposition. New zero invariant or optimizing a growing polynomial goes to B03. Outputs only notes/06_VCD_E06_EXPONENTIAL_SCORE_RESIDUAL_20261116.md and research-progress/handoffs/VCD-E06-r1-return.md. No status/index/chat edits.

## Pinned inputs
- `papers/investigations-6/03_volterra_coefficient_dynamics/brainstorm/notes/04_VCD_B02_SCORE_INFORMATION_DECISION_20261116.md` SHA-256 `6dc1ea4600f93f9c78451778c499c566f739fd36e9d55966d78f1255056b7d38`
- `papers/investigations-6/03_volterra_coefficient_dynamics/manuscript/main.tex` SHA-256 `18346543517c374c5e55d095b6c6847a0ef21f2e18917fff428d54901cf60dcc`
- `papers/investigations-6/03_volterra_coefficient_dynamics/notes/01_VCD_E01_LOGARITHMIC_ENVELOPE_20261113.md` SHA-256 `4a20a5806715a0950cac79271cbe69d901188c489a2ea6889c4f75996af6577b`
- `papers/investigations-6/03_volterra_coefficient_dynamics/notes/05_VCD_E05_SOURCE_SCORE_RESIDUAL_20261116.md` SHA-256 `a493aaa6eb3d648eb8baa15087dcc3daf11bf071337c7c901856ea5f186e027a`
