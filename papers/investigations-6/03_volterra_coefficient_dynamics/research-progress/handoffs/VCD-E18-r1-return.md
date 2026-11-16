# VCD-E18 r1 — exterior anchor comparison return

16 November 2026, America/New_York. Prepared for Edward Baker with
OpenAI Codex LLM assistance. Recorded task dispatch **gpt-6.1-sol / ultra**.
Separate runtime model and effort attestation unavailable.

**Complete, proved in-note.** [Note 17][note] executes [E18 r1][request].
All five pinned input hashes match. The note SHA-256 is
\(\texttt{9107548241452dd34c4426dd749380ab91afd8711905802f88966a1a2a375c70}\).
One analytical proof and one correction pass were used. Both requested
algebraic formulas are confirmed. The correction pass clarified the
exterior arguments used in the uniform Stirling expansion.

With the exact canonical \(b\) and \(F_\pm=F(z\pm4i)\), integration
by parts gives \(4\pi(F_--F_+)+B=izF\). At \(z=x+iy\),
\(0<y<1\), set \(s=(1-iz)/2\). The arguments \(s+2\) and \(3-s\)
for the two anchors lie in \(\operatorname{Re} w>2\).
Both anchors are nonzero there. The larger anchor has magnitude
comparable to \(e^{-\pi x/8}x^{(11+y)/4}\) as \(x\to+\infty\),
and \(|F_-/F_+|=O(x^{-y/2})\), uniformly on every closed
subinterval of \(0<y<1\). Therefore
\(\Delta=4\pi(|F_+|-|F_-|)\) is eventually positive and comparable to
the larger scale. Pointwise, \(|B|<\Delta\) implies
\(|F(z)|\ge(\Delta-|B|)/|z|>0\).

The exact normalized remainder is
\[
 \frac{B}{4\pi F_+}
  =1-\frac{F_-}{F_+}
    -\frac{(2s-1)(s-1)}{2(s+2)(s+1)}
     \frac{\zeta(s)}{\zeta(s+2)}.
\]
The denominator \(\zeta(s+2)\) is nonzero by the exterior Euler
product. For \(\operatorname{Re}s>1\), the quotient has coefficients
\(a_n=\prod_{p\mid n}(1-p^{-2})\) with \(a_1=1\) and
\(1/\zeta(2)\le a_n\le1\). This proves divergence of the absolute
coefficient sum for \(\operatorname{Re}s\le1\). The continued quotient
is holomorphic in the comparison strip. The comparison needed to
make the reverse-triangle lower bound positive is open.

Checked passages, 16 November 2026, forwarded to the lead for
cataloging. Riemann's 1859 paper, *Ueber die Anzahl der Primzahlen
unter einer gegebenen Grösse*, Monatsberichte der Berliner Akademie,
pp. 671–680, was inspected in David R. Wilkins's English translation,
printed pp. 1–4. It supplies the product, completion and reflection.
Rodgers–Tao, arXiv:1801.05914v5, 3 July 2021, §1 equations (1)–(3)
and the following evenness passage, confirms the half-line normalization.
Checked NIST DLMF passages are (25.2.1), (25.2.11), (25.4.3)–(25.4.4),
§5.2(i), (5.5.1), (5.11.1), (5.11.9), and the opening remainder
paragraph of §5.11(ii). These are online passage inspections, with
no local reading copies created by E18. [Riemann][riemann]
[Rodgers–Tao, arXiv v5][rt] [Series and product][euler]
[Xi reflection][xi] [Gamma definition][gamdef]
[Gamma recurrence][recurrence] [Stirling and errors][stirling]

## Response addendum — frozen E17 result

The completed [E17 return][e17return] has SHA-256
\(\texttt{e5769709f7623e4761d1e532c033b615b77ef35588ff474ffe58c0ebee05d37d}\).
It confirms the fixed-\(Y\) optimized allowance
\(\frac{15}{Z(1-Y)}(ex/14)^{7/2}e^{-\pi x/8}\) asymptotically.
For each fixed \(0<y\le Y<1\), its ratio to \(\Delta\) grows
comparably to \(x^{(3-y)/4}\). Thus the optimized bound from that
termwise-absolute majorant exceeds the sufficient margin at large
\(x\). The actual remainder and sharper bounds retaining cancellations
remain open.

[request]: VCD-E18-r1.md
[note]: ../../notes/17_VCD_E18_EXTERIOR_ANCHOR_COMPARISON_20261116.md
[e17return]: VCD-E17-r1-return.md
[riemann]: https://www.maths.tcd.ie/pub/HistMath/People/Riemann/Zeta/EZeta.pdf
[rt]: https://arxiv.org/pdf/1801.05914v5
[euler]: https://dlmf.nist.gov/25.2
[xi]: https://dlmf.nist.gov/25.4
[gamdef]: https://dlmf.nist.gov/5.2.i
[recurrence]: https://dlmf.nist.gov/5.5.E1
[stirling]: https://dlmf.nist.gov/5.11
