# Riemann's theta–Mellin formula: book equation (2.1)

28 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), recorded effort xhigh**,
chat0016. Selected passages only; no full-paper or whole-chapter audit.

## Riemann, 1859

Bernhard Riemann, *Ueber die Anzahl der Primzahlen unter einer gegebenen
Grösse*, Monatsberichte der Berliner Akademie, November 1859. Version
read: David R. Wilkins's English translation, *On the Number of Prime
Numbers less than a Given Quantity*, preliminary version December 1998.
[Primary-hosted translation](https://www.maths.tcd.ie/pub/HistMath/People/Riemann/Zeta/EZeta.pdf).

Checked printed p.3 (PDF page4): the theta series, its Mellin integral,
the Jacobi transformation, and the split-at-one continuation with rational
term 1/[s(s-1)]. Riemann's Pi(s/2-1) is modern Gamma(s/2). The initial
theta integral converges for Re(s)>1; the split formula provides
meromorphic continuation. The book's V-kernel form follows by the direct
recombination in [Note35](../notes/35_CLASSICAL_THETA_MELLIN_ATTRIBUTION_20261028.md).
The printed source is not being claimed to use the exact V notation.
Only extracted primary text was inspected; the optional browser screenshot
was unavailable. No claims from the later prime-counting argument are used.

External reading-copy receipt (retrieved 28 October 2026):

```json
{
  "source_url": "https://www.maths.tcd.ie/pub/HistMath/People/Riemann/Zeta/EZeta.pdf",
  "archive_path": "/Users/Shared/szp-archive/radial-theta-collision-geometry/references/Riemann_1859_Wilkins_translation_199812.pdf",
  "bytes": 119504,
  "sha256": "6b24341e3406d165baeb7ab1e00cfa0a544d0399e2b33175dfa71480bdddd24f",
  "status": "Public translation reading copy archived outside Git"
}
```

## Existing NIST DLMF source: additional checked passages

The existing DLMF catalog entry is extended rather than duplicated.
Online version shown: 1.2.8, released 15 September 2026; retrieved
28 October 2026.

- [25.5.13](https://dlmf.nist.gov/25.5.E13) and
  [25.5.14](https://dlmf.nist.gov/25.5.E14): modern split theta formula and
  theta-tail definition; the source attributes the formula to Titchmarsh,
  1986, p.22. That book itself was not independently inspected here.
- [25.4.4](https://dlmf.nist.gov/25.4.E4): xi normalization, including the
  factor one-half and s(s-1). This fixes the sign in the V-kernel identity.

Note35 supplies the variable substitution x=r^2, elementary split, exact
strip and the distinction between convergence and continuation. These
sources establish the classical scalar identity; they do not establish
novelty or non-novelty of the separate geometric or flow constructions.
No artificial DLMF PDF was created.
