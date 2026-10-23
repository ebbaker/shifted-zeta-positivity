# Fixed canonical jet bulk lower bound contract

22 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance; actual recorded gpt-6.1-sol, effort ultra.

Before execution, fix the unchanged zero-time theta field H0=xi((1+iz)/2)/8 and its existing degree64, radius16 Cauchy oracle on |z-35|<=8. The target is a positive lower bound for Note10's M_phi, not a phase sign or a simplicity certificate. Use its rectangle C=35,L=h=4sqrt(2), and the one disk |z-(35+2i)|<=1. No adaptive geometry, mesh scan, root lookup or new cutoff optimization.

On this disk phi>=m_phi=(31/32)^3(23/32)^3. The ordinary holomorphic submean inequality gives

M_phi >= m_phi pi |J'(35+2i)|^2 / sup_disk |J|,

where J=H0+iH0'. Acquire the center lower bound and full-disk upper by shifting the existing exact Taylor coefficient balls to 35+2i, retaining complete errors epsilon_J<=epsilon_H+epsilon_H' and epsilon_J'<=epsilon_H'+epsilon_H''. The source is not replaced by its finite polynomial. All coefficient balls, modulus, source-tail and rounding uncertainties remain in the bound. No zero, branch or physical jet floor is assumed.

Arithmetic: python-flint0.9 Arb at192bits. One oracle setup and one fixed point/disk evaluation, no numerical area quadrature. Stop if any finite, positivity or geometry check fails. Success means a complete positive lower bound which also exceeds the existing potential-source error8.05e-19; failure is recorded without changing the contract. A passing bound can subtract from any independently acquired upper for P_phi, but acquires no P_phi or T_phi sign itself. The equally informed direct estimator receives the same point, source oracle and lower-mass identity.

The small receipt pins the script, oracle and contract hashes and records outward exact rational endpoints. All outputs stay below1MiB. A separate same-model review is required before treating the receipt as accepted internal numerical evidence; no specialist validation is claimed.
