# DLMF gamma and zeta identities for the canonical floor ceiling

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort ultra**.

**Source:** National Institute of Standards and Technology, *NIST Digital
Library of Mathematical Functions*. Online reference, retrieved
26 October 2026 in America/New_York.
Only the passages below were checked; no full chapter audit is claimed.
The live online pages are not treated as version-pinned articles.

| Passage | Checked content and use |
| --- | --- |
| [5.4.3](https://dlmf.nist.gov/5.4.E3) | Exact modulus of Gamma(iy), real y. Combined with recurrence to obtain the squared modulus pi v/sinh(pi v) of Gamma(1+iv), v>0. |
| [5.5.1](https://dlmf.nist.gov/5.5.E1) | Gamma(z+1)=z Gamma(z). |
| [25.2.1](https://dlmf.nist.gov/25.2.E1) | Absolutely convergent ordinary zeta series for Re s>1; at Re s=2 the triangle inequality bounds the modulus of zeta(s) by zeta(2). |
| [25.6.1](https://dlmf.nist.gov/25.6.E1) | zeta(2)=pi^2/6. |
| [5.11.1 and 5.11.3](https://dlmf.nist.gov/5.11) | Gamma asymptotics in closed sectors avoiding the negative real axis. Only the positive-real consequence log Gamma(v)=O(v log v) is used for the coarse Jensen count. |

The canonical formula H(0,z)=xi((1+iz)/2)/8 and its factor 1/16 in
front of s(s-1)Gamma(s/2)zeta(s) are inherited from the repository's
[Book canonical definition](../../01_heat_density_asymptotics/book/sections/01_canonical.tex).
The new application at z=3X/2-3i has Re s=2, so no critical-strip zeta
bound, RH-dependent zeta estimate or unproved lower bound is imported.
The floor **ceiling**, count upper bound and optimized sufficient-allowance
failure are derived in [Note03](../notes/03_CANONICAL_FIXED_STRIP_ALLOWANCE_FAILURE_20261026.md).

DLMF 25.10 was also inspected for context; no zero-count asymptotic from
it is imported. Jensen's formula and the source envelope in Note03 give
the count upper bound directly. These online-reference records require
no artificial PDF copy under the repository reference workflow.
