# Complete xi quadrature source passages

16 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. E08 helper dispatch was
**gpt-6.1-sol / ultra**. Lead settings and separate backend attestation
are unavailable.

Inspected the indicated equations in the official NIST *Digital
Library of Mathematical Functions*, online release 1.2.8,
15 September 2026, on 16 November 2026. Scope is the exact passages and
their displayed hypotheses. The permanent equation links below serve
as reading records. The canonical DLMF bibliography record remains
with the [parent VCD catalog](../../references/README.md).
[NIST release information](https://dlmf.nist.gov/about/).

| Official passage | Checked input and use |
| --- | --- |
| [DLMF 5.9.10_2](https://dlmf.nist.gov/5.9#E10_2), Binet's formula | The complex log-gamma identity has a Laplace remainder with kernel \((1/(e^v-1)-1/v+1/2)/v\), valid for \(|\arg\omega|<\pi/2\). Note12 §2 bounds the kernel by \(1/12\) using elementary hyperbolic-function series, then checks the phase term to retain \(\exp(-\pi|\Im\omega|/2)\). DLMF attributes the identity to Whittaker and Watson, *A Course of Modern Analysis*, 1927, §12.31. The inspected passage was the NIST formula. |
| [DLMF 25.2.8](https://dlmf.nist.gov/25.2#E8), Euler–Maclaurin representation | The integral with fractional-part kernel and integer \(N\ge1\) applies on \(\Re s>0\), with \(s=1\) the pole. Taking \(N=1\) and then \(\Re s\ge1/2,\ |\Im s|>7002\) gives the elementary bound \(|\zeta(s)|\le3|s|\) used in Note12 §2. DLMF attributes the displayed formula to Apostol, *Introduction to Analytic Number Theory*, 1976, (25), p. 269. The inspected passage was the NIST formula. |
| [DLMF 25.4.3](https://dlmf.nist.gov/25.4#E3) and [25.4.4](https://dlmf.nist.gov/25.4#E4), completion and reflection | The reflected completed function is \(\xi(1-s)=\xi(s)\), with the factor \(s(s-1)\pi^{-s/2}\Gamma(s/2)/2\) multiplying \(\zeta(s)\). Note12 §1 derives the physical \(H_0=\xi((1+iz)/2)/8\) from the inherited theta Mellin identity. Note12 §2 uses reflection to work only with \(\Re s\ge1/2\). |

The [E08 proof](../notes/12_VCD_GT_E08_CANONICAL_XI_ORACLE_20261116.md)
derives the two-strip-line trapezoid bound from periodization and
contour shifts and pays the finite lattice tails separately. The
canonical pair article is recorded in
[the branch's Lehmer source addendum](01_VCD_GT_LEHMER_SOURCE_USE_20261116.md)
under its own scope.

## Gamma-transform passage, 17 November 2026, chat0007

Prepared for Edward Baker with OpenAI Codex assistance; actual model and
effort unavailable. Reused the canonical DLMF record and inspected
[5.9.1](https://dlmf.nist.gov/5.9.E1) and its displayed hypotheses online.
With its exponent parameter set to one, it gives
\(a^{-p}=\Gamma(p)^{-1}\int_0^\infty s^{p-1}e^{-as}\,ds\) for
\(\Re a>0,\Re p>0\), with principal powers. The use in
[hierarchy discussion44](../notes/44_VCD_GT_SCALE_AND_MOMENT_HIERARCHY_DISCUSSION_20261117.md)
is a conditional connection between reciprocal interaction powers and
Gaussian/Laplace scales. The nearby complex denominators need not have
positive real part, and the complete sum needs its own convergence
justification. No analytic continuation across that sector boundary or
canonical sign estimate is imported. Passage inspection only; no PDF
download, new release-version claim or full chapter audit.
