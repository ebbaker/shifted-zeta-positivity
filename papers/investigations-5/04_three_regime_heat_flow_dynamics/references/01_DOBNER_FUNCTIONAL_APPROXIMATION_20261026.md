# Dobner functional approximation and the joint limit

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**.

## Source and checked scope

Alexander Dobner, *A proof of Newman's conjecture for the extended Selberg
class*, Acta Arithmetica **201** (2021), 29–62,
[DOI 10.4064/aa200603-23-7](https://doi.org/10.4064/aa200603-23-7).
Version read: [arXiv:2005.05142v2](https://arxiv.org/abs/2005.05142v2),
10 January 2026. Retrieved 26 October 2026.

Checked in the [primary HTML](https://arxiv.org/html/2005.05142v2):
normalization (5)–(6); Theorem4 and (10)–(13); Section3.1 and Theorem5;
Lemma3's proof; Section4.1, especially (35). Selected proof passages,
not a full proof audit. Earlier introductory inspection remains recorded
in [02's catalog](../../02_heat_flow_rh_applications/references/README.md).

The method combines a Gaussian-damped Dirichlet series, almost periodicity
and Rouché transport to obtain nonreal zeros at each fixed negative time.
Lemma3 obtains a seed zero through factorization and Dirichlet-series
uniqueness. This proves nonnegativity, shared by our three regimes.

## Published input in canonical coordinates

Write \(t=-\tau<0\), \(w=x+iy\), and specialize to zeta. Set

\[
Z_\tau(w)=\sum_{n\ge1}e^{-\tau(\log n)^2/4}n^{-w},\qquad
J_{-\tau}(w)=w+\frac\tau4\operatorname{Log}\frac{w}{2\pi},
\]

\[
\gamma(w)=\tfrac12w(w-1)\pi^{-w/2}\Gamma(w/2),\qquad
\gamma_{-\tau}(w)=\gamma(w)e^{(w-J_{-\tau}(w))^2/\tau}.
\]

Theorem4 gives

\[
\frac{\xi_{-\tau}(J_{-\tau}(w))}{\gamma_{-\tau}(w)}
=Z_\tau(w)+E_\tau(w),\qquad
|E_\tau(w)|\le K_Cy^{-1/5}
 e^{10\min(x,-2)^2/\tau},
\tag{D1}
\]

for \(0<\tau\le C\), \(|x|\le Cy^{1/4}\),
\(y\ge y_0(C)\); constants also depend on the fixed completed function.
Equation (35) retains the sharper bound

\[
|E_\tau(w)|\le K_C\left(y^{-1/5}Z_\tau(x)
 +e^{-y^{2/3}/(20\tau)}\right).
\tag{D2}
\]

The heat-time normalization agrees with ours:
\(\xi_t((1+iz)/2)=8H(t,z)\). The map acts before rotation to z.
Theorem4 exposes time dependence; its qualitative fixed-time corollary
does not make the error uniformly small as \(\tau\downarrow0\).

## Budget consequences to investigate

The following calculations are our deductions from (D1), not additional
claims of the paper. They specify the missing quantitative inputs for
[TRD-03](../research-progress/01_THREE_REGIME_DYNAMICS_RESEARCH_PROGRESS_20261026.md).

Suppose a seed disk for \(Z_\tau\) has boundary \(C_\tau\), real-coordinate
range \([\alpha_\tau,\beta_\tau]\), at least one zero inside, and floor
\(\delta_\tau=\min_{C_\tau}|Z_\tau|>0\). Let
\(B_\tau=\max(2,-\alpha_\tau)\). On a vertical translation whose entire
disk lies at height \(y\ge Y\), the approximation allowance is at most
\(\delta_\tau/3\) if

\[
\log Y\ge\frac{50B_\tau^2}{\tau}
       +5\log\frac{3K_C}{\delta_\tau},
\tag{D3}
\]

together with the domain restrictions in (D1). To put the entire mapped
disk to the right of \(\Re w=1/2+d\), with \(d>0\), it suffices that

\[
\log Y\ge\log(2\pi)
       +\frac4\tau\left(\frac12+d-\alpha_\tau\right).
\tag{D4}
\]

Indeed \(\Re J_{-\tau}(w)=x+(\tau/4)\log(|w|/(2\pi))\).
Include \(Y\ge y_0(C)\) and
\(Y\ge(\max(|\alpha_\tau|,|\beta_\tau|)/C)^4\).
Choose a translation for which the almost-period error on the seed
boundary is less than \(\delta_\tau/3\). The two errors then leave a
positive Rouché margin. The rotated zero has \(|\Im z|\ge2d\), and its
horizontal coordinate equals twice the mapped imaginary coordinate.

This conditional budget displays an exponential scale in \(1/\tau\)
when the strip and margin remain controlled. It supplies no universal
onset law: the seed's position and margin may vary with \(\tau\), and
an upper bound on a suitable translation height is still needed.
The constants in (D1) have not been made numerically explicit here.

The first comparison should retain (D2) and the actual coefficients,
instead of paying the final coarse exponential majorant automatically.
Measure improvement against the *combined* seed, recurrence and field
budget. An upper bound for one constructed witness cannot exclude nearer
nonreal zeros; any comparison with compact escape must preserve that
direction of implication.

Likewise, a putative positive threshold T changes the base source to
\(e^{Tu^2}\Phi(u)\). The formal positive-time coefficient multiplier
\(e^{T(\log n)^2/4}\) destroys ordinary Dirichlet-series convergence in
every fixed right half-plane. Applying the same theorem at a shifted base
therefore requires a new representation or a new hypothesis check.
This is a proposed research issue, not an obstruction to all functional
approximation methods for positive thresholds.

## Archive identity

The existing authorized PDF was reused and its header, size and hash
rechecked; no third-party PDF was added to the repository.

- Public PDF: [2005.05142v2](https://arxiv.org/pdf/2005.05142v2).
- Archive: `/Users/Shared/szp-archive/height-dependent-heat-contours/references/2005.05142v2.pdf`.
- Size: **734966 bytes**.
- SHA-256: `4f7958bbd64bc386afdfe4c2e50f27535b688d2bded15714e6e8e679a90b2422`.
- Original receipt: [HDC download manifest](../../../investigations-4/12_height_dependent_heat_contours/references/REFERENCE_DOWNLOAD_MANIFEST_20261023.json).

The hash identifies a reading copy and does not validate the argument.
The [reference workflow](../../../../REFERENCE_WORKFLOW.md),
[result index](../../../../result-summaries/README.md) and
[unchecked-import guidance](../../../../avoid/16_unchecked_imports_and_novelty_claims.md)
govern further use.

## Subsequent quantitative seed use

26 October 2026, prepared for Edward Baker with substantial LLM assistance,
**gpt-6.1-sol (Codex), actual recorded effort ultra**. Rechecked the same
version's Theorem4, equations(11)-(13), Section3.1, Lemma3 and equation35,
especially that C=1 fixes constants uniformly for0<tau<=1 while the
growing real-coordinate strip still requires |x|<=y^{1/4}. Theorem4 also
allows each fixed C>=32 for the separate direct-lattice construction.
No numerical K_C or y_0(C) has been acquired, and no full proof audit is
claimed. The existing archived PDF was reused; no new PDF was downloaded.

[Note03](../notes/03_SMALL_TIME_CANONICAL_SEEDS_AND_WITNESS_ENVELOPE_20261026.md)
supplies our analytical seed/count/wall family and uniform source-derived
witness upper envelope; [Note04](../notes/04_DIRECT_DOBNER_SEED_LATTICE_20261026.md)
supplies our direct seed lattice for tau>=32. These quantitative seed
derivations are not attributed to Dobner's paper, and their recording
makes no literature-priority claim. [Review02](../reviews/02_DOBNER_CANONICAL_SEED_ACQUISITION_REVIEW_20261026.md)
records internal same-model checks and the remaining limitations.

**27 October 2026 subsequent use**, prepared for Edward Baker with
substantial LLM assistance, **gpt-6.1-sol, actual effort ultra**:
[Note05](../notes/05_NARROW_SMALL_TIME_DOBNER_SEEDS_20261027.md) supplies our
narrower canonical seed construction and improved full witness envelope;
[Summary06](../notes/06_CHAT0001_RESEARCH_SUMMARY_20261027.md) consolidates
the chat. Theorem4 and equation35 were rechecked for fixed C=1, with the
same normalization/domain and uninstantiated K_1,y_0(1). The Gaussian
integral comparison and moment bounds are proved directly in Note05;
no tabulated special-function zero or new external identity is imported.
These are our deductions, not additional claims attributed to the paper.
No new PDF or full proof audit was undertaken.
