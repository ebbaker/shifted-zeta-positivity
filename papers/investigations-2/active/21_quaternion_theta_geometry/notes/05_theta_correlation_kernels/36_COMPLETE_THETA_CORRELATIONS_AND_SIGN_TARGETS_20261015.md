---
research_program: PR02-CORR
parent_program: PR02
secondary_programs: [ALG, PR03]
status: exact_reduction_and_open_target
---

# Complete theta correlations and stationary sign targets

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded model **gpt-6-astra**, reasoning effort **ultra**. This note develops the actionable correlation route in [Review 25](../../reviews/25_OCTONIONIC_MACHINERY_LITERATURE_REVIEW_20261015.md). The [current overview](../../research-overview/RESEARCH_OVERVIEW_20261015_CORRELATION_KERNELS.md) places it within PR02. All identities below use the complete theta source; the new theta-specific lower bound remains unproved.

## Normalization and complete correlations

Extend \(w_t(u)=e^{tu^2}\Phi(u)\) evenly to the real line. Then

\[
2H(t,x)=\int_{\mathbb R}w_t(u)e^{ixu}\,du.
\]

The complete source and its polynomially weighted heat deformations are integrable on compact parameter sets. For \(m\ge0\), put

\[
K_m(t,s)=\int_{\mathbb R}r^{2m}w_t(s+r)w_t(s-r)\,dr.
\]

Polarization and \(u=s+r,v=s-r\), with Jacobian two, give

\[
\boxed{\mathcal L_0(t,x)=\int_{\mathbb R}K_1(t,s)\cos(2xs)\,ds,}
\]

\[
\boxed{\mathcal L_1(t,x)=\int_{\mathbb R}
\{K_2(t,s)-s^2K_1(t,s)\}\cos(2xs)\,ds.}
\]

To check constants, let \(F=2H\). The symmetrized multipliers for \(F'^2-FF''\) and \(F''^2-F'F'''\) are respectively \((u-v)^2/2\) and \(-uv(u-v)^2/2\). Substitute \(u-v=2r\), \(uv=s^2-r^2\), and divide by four. Both paired sectors and all source-index interactions are retained in the resulting formulas.

The energy has the compatible representation

\[
B(t,s)=\tfrac12\{(1-s^2)K_0(t,s)+K_1(t,s)\},
\qquad E(t,x)=\int_{\mathbb R}B(t,s)\cos(2xs)\,ds.
\]

Here \(B(t,s)\) is a correlation density, distinct from the optional cutoff observation \(B_N\) in Note 35. It need not be pointwise nonnegative even though its displayed transform equals the nonnegative energy.

The heat deformation remains explicit:

\[
K_m(t,s)=e^{2ts^2}\int_{\mathbb R}r^{2m}e^{2tr^2}
\Phi(s+r)\Phi(s-r)\,dr,
\quad\partial_tK_m=2s^2K_m+2K_{m+1}.
\]

Consequently

\[
(\partial_t+\partial_x^2)\mathcal L_0=2\mathcal L_1.
\]

This exact identity relates the observations; it does not eliminate either stationary condition or give a forward minimum principle.

The associated-kernel method appears in [Csordas, Theorem 3.7](https://arxiv.org/pdf/1309.0055); [Dimitrov–Xu](https://arxiv.org/pdf/1606.05011) develops a broader Wronskian/Fourier framework. The present identities were derived directly with the manuscript's normalization. They do not assume that the heat-deformed source satisfies every hypothesis of those authors' positivity theorems.

## The original hybrid cutoff in the same coordinates

Preserve the manuscript's analytic contour shift \(a\), source terms \(\phi_n\), and staircase cutoff. Write \(d_n=\tfrac12\log n\), \(V_N=\tfrac12\log N\), and

\[
\psi_{a,N}(t,y)=e^{t(y+ia)^2}
\sum_{y+d_n\le V_N}\phi_n(y+ia)\quad(y\ge0),
\]

with value zero for \(y<0\). Its support is contained in \([0,V_N]\). The retained shifted jet is

\[
h_k^{(N)}=e^{-ax}\Re\int_0^{V_N}
(-a+iy)^k\psi_{a,N}(t,y)e^{ixy}\,dy.
\]

Define the mixed correlation

\[
\mathscr C_{j,N}^{a}(t,s)=
-\int_{s-V_N}^{s}[i(s+r)]^j[-a+i(s-r)]^{j+2}
w_t(s+r)\psi_{a,N}(t,s-r)\,dr.
\]

Then, without replacing full stationarity by retained stationarity,

\[
\boxed{J_{j,N}=-h_jh_{j+2}^{(N)}
=e^{-ax}\Re\int_{\mathbb R}
\mathscr C_{j,N}^{a}(t,s)e^{2ixs}\,ds.}
\]

Indeed the factor \(1/2\) in the full-line formula for \(h_j\) cancels the Jacobian two. Since \(h_j\) is real, the real part can be taken after multiplying the integrals. The domain \(0\le y=s-r\le V_N\) gives the stated bounds on \(r\). Every staircase discontinuity remains inside \(\psi_{a,N}\).

The original complete source-tail bounds still apply. Differentiating or integrating by parts in these coordinates requires retaining staircase-entry and boundary terms; the change of variables does not cancel them. This mixed correlation is the preferred finite-resolution bridge to the existing transfer theorem, rather than a new arbitrary cutoff.

## Open signed targets

Let \(A_0=K_1\) and \(A_1=K_2-s^2K_1\). The full target is

\[
\int_{\mathbb R}\{A_j(t,s)+\kappa_j(t,x)B(t,s)\}
\cos(2xs)\,ds\ge0\quad\text{on }S_j,
\]

with \(\kappa_j\ge0\) prescribed from the source and locally bounded through every covered finite positive-time candidate event. This is exactly \(\mathcal L_j\ge-\kappa_jE\), with no division by the possibly vanishing energy. Because \(\kappa_j\) can depend on \(x\), the expression is generally not one global positive-definite-kernel problem.

An alternative is a paid mixed-correlation lower bound, for every \(N\ge N_0\),

\[
J_{j,N}\ge-\alpha_j(t,x)N^pE-
\beta_j(t,x)e^{-cN^2},
\]

with fixed finite \(p\ge0\), \(c>0\), and all source-prescription/local-boundedness hypotheses of the manuscript's conditional transfer. This notation records the target shape; the exact tail parameters and permitted coefficients must match the adopted source envelopes. The complete tail payment and Young's inequality then give the established logarithmic-loss criterion.

The new estimate may be restricted to \(E\le\delta\Gamma^2\) for fixed \(\delta>0\), using the explicit nonzero Stirling scale \(\Gamma\), on a declared domain covering the needed predecessor curves. Existing absolute bounds handle the complement. This localization assumes no energy floor near a collision.

Pointwise \(K_1>0\) is not Fourier-transform positivity. Nor does \(K_2-s^2K_1\) have an automatic pointwise sign. A positive-definite decomposition with a paid signed remainder would suffice, but demanding a global positive-definiteness theorem is stronger than this stationary target.

## What an arithmetic mechanism must add

In the underlying theta factors, put

\[
y_+=e^{4(s+r)},\qquad y_-=e^{4(s-r)},\qquad y_+y_-=e^{8s}.
\]

They are reciprocal only for \(s=0\). Modular inversion therefore does not automatically diagonalize the full two-variable product. After using the theta identity to establish source evenness, inversion of one factor exchanges \(s\) and \(r\), up to signs. This symmetry also holds for arbitrary even sources, including collision controls, so it cannot be the new input by itself.

The heat multiplier in the modular variable is \(\exp\{t(\log y)^2/16\}\). It respects inversion but is not a fixed modular weight. Any proposed transformed identity must retain it, the differential factors producing \(\Phi\), and all retained/omitted cross interactions.

A useful candidate must therefore identify a genuinely theta-specific identity among the full amplitudes and show where its signed cancellation pays the adverse part of \(A_j\) or \(\mathscr C_{j,N}^a\). It should first be checked against the manuscript's positive-source collision controls: if the proof uses only properties shared by those controls, the claimed exclusion cannot follow.

## Conditional literature-to-identity tests

The exact literature survey and publication metadata remain in Review 25. Its actionable leads are:

- Modular sign constructions in Viazovska, Romik and Lee can suggest how to preserve a combined modular expression before estimation. First exhibit the exact deformed correlation belonging to an applicable class; a similar Fourier sign problem is not an identity.
- Integral octonions and exceptional theta lifts offer genuine arithmetic summation identities. First produce a restriction/transform recovering this Jacobi-theta source and its physical observation. The \(E_8\) lattice theta series has different coefficients and Mellin factors, so it cannot be substituted for \(H\).
- Hardy/Bergman or Teodorescu operators can support a specified boundary/defect estimate, but must yield the signed physical-energy payment rather than merely an absolute norm bound.
- Phase/Wronskian and de Branges formulations require their own exact positivity hypothesis. Counterexamples to specific de Branges shift-positivity proposals do not rule out the entire framework, but they preclude treating such positivity as automatic.

These are bounded applicability tests within PR02-CORR, not additional principal programs.

## Pilot, acceptance and continuation

1. Declare one complete theta identity, the resulting signed observation, its domain, and a source-derived coefficient family. Include both \(S_0\) and \(S_1\) and explain coverage of predecessor neighborhoods.
2. Specify all source/analytic cutoffs, Gaussian tails, boundary terms and derivative errors before computation. Choose precision from the cancellation budget.
3. Test predetermined theta values, including below two, on genuine full stationary points. Freeze the coefficient rule before fresh validation cells; do not infer it from a quotient by a sampled energy floor.
4. A certified violation rejects the declared mechanism. An undecided enclosure requires refinement or a different test, not a mathematical verdict.
5. A successful pilot must lead to an unbounded-domain lemma and a coverage argument. Finite favorable samples or drifting asymptotic thresholds do not establish global exclusion.

The Gaussian control \(w(u)=e^{-u^2}\) checks the normalization: \(H=\sqrt\pi e^{-x^2/4}/2\) and \(\mathcal L_0=\pi e^{-x^2/2}/8\), agreeing with the correlation formula. This verifies constants in a control case, not a new theta sign certificate. Numerical scripts and small receipts belong in `numerics/`; independent assessments belong in `reviews/`.

The [181-assertion exact checker](../../numerics/check_theta_correlation_identities.py) and [execution record](../../numerics/THETA_CORRELATION_IDENTITY_CHECKS_20261015.json) check the correlation multipliers, Gaussian normalization, heat/energy algebra, and independently integrated hybrid polygon moments. [Review 26](../../reviews/26_OCTONIONIC_CORRELATION_MANUSCRIPT_INTEGRATION_20261015.md) records the integrated proof and scope audit.
