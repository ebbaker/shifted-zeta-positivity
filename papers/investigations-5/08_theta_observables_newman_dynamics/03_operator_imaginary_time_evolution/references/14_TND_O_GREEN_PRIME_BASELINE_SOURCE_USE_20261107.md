# Green-potential prime baseline: exact source use

6 November 2026 America/New_York (7 November UTC). Prepared for Edward Baker with substantial Codex assistance; lead tool-selected gpt-6-astra/ultra, not independent backend verification.

For the post-E16 B04 comparison, freshly inspected the following primary DLMF pages, version1.2.8 (release15 September2026 as shown by the site):

- [25.2(i),(iv), equation25.2.11](https://dlmf.nist.gov/25.2): zeta's sole simple pole at1 with residue1 and its Euler product for Re s>1. The logarithmic Dirichlet series used in the reduction is derived by the absolutely convergent expansion of each Euler factor, with coefficient Lambda_vM(n)/log n. Here Lambda_vM denotes von Mangoldt, not the Newman threshold.
- [25.4, equations25.4.3–4](https://dlmf.nist.gov/25.4): xi reflection and xi=s(s−1)Gamma(s/2)pi^(−s/2)zeta(s)/2. With H0(z)=xi(1/2+iz/2)/8, reflection permits s=1/2−iz/2, placing the upper strip at Re s>=1/2.
- [5.2(i)](https://dlmf.nist.gov/5.2): Gamma has no zeros and poles only at the nonpositive integers. Thus its factor is zero-free throughout this strip.
- [5.11(i), equation5.11.1](https://dlmf.nist.gov/5.11): logarithmic Stirling growth in a fixed sector away from the negative real axis. This gives at most polynomial/logarithmic growth for the gamma-factor log modulus on the finite-width s strip; exponential Poisson kernels pay it.

The consuming calculation is the λ=0 Green arithmetic comparison in B04 r4 Decision15. Safe lines at Im z=4,8 become Re s=5/2,9/2. The factor s−1 has its zero at z=i and supplies +G(X,1); it must not be lost by treating log zeta as harmonic across its pole. Constants, s, pi^(−s/2), and Gamma(s/2) contribute zero to the complete strip boundary-minus-interior functional after their harmonic growth is paid.

The exact prime baseline and its uniform index tail are derived locally from these identities and Note25, not imported as a new literature theorem. No novelty claim, full-paper audit, new third-party PDF or numerical evaluation is made. Existing canonical DLMF ownership is reused; this is a selected-passage use receipt, not a duplicate bibliography catalog.
