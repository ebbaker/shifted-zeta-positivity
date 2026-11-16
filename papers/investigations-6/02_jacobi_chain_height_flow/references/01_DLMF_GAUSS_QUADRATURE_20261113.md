# DLMF — Gaussian quadrature and Jacobi truncations

13 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex assistance; dispatch selection **gpt-6-astra / ultra**;
actual backend model/effort unavailable.

**NIST Digital Library of Mathematical Functions**, Chapter 3,
[§3.5(v)](https://dlmf.nist.gov/3.5#v) and
[§3.5(vi)](https://dlmf.nist.gov/3.5#vi), online version retrieved
13 November 2026 local date. The displayed release version was not recorded.
No PDF copy is needed for this online reference.

Inspected equations 3.5.18–3.5.20_2 and 3.5.30–3.5.33: positive quadrature
weights, exactness through degree (2N-1), monic squared norm as the
remainder constant, finite Jacobi eigenvalues as nodes, and first-component
squares as weights. Positive measures on finite or infinite intervals
with the needed moments are the relevant setting. The real-valued
derivative remainder is the precedent; E01 will supply its own pointwise
Hermite argument and integration for cosine on the full line.

[§3.3(i)](https://dlmf.nist.gov/3.3#i), equation 3.3.5, was also inspected
for the real interpolation remainder and its smoothness/real-node
conditions. §3.3(vi) mentions Hermite interpolation but does not provide
the proof needed here. No claim of full chapter reading is made.

Used by [JCH-B01](../brainstorm/notes/01_JCH_B01_READOUT_DECISION_20261113.md)
and its [source/control screen](../notes/01_JCH_B01_SOURCE_AND_CONTROL_SCREEN_20261113.md).
The heat averaging and explicit complete-source envelope are derivation
targets of JCH-E01, not attributed to DLMF. This is classical quadrature
applied to the inherited theta chain; no novelty claim or unseen theorem
import. See the local [BibTeX](jacobi_chain.bib).
