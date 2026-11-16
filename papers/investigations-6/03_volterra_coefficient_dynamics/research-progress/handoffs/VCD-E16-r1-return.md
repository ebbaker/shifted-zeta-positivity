# VCD-E16 r1 — midpoint calibration bound return

16 November 2026, America/New_York. Prepared for Edward Baker with
OpenAI Codex LLM assistance. Recorded task dispatch **gpt-6.1-sol / ultra**.
Separate runtime model and effort attestation unavailable.

**Complete, proved in-note.** [Note 14][note] executes [E16 r1][request].
All four pinned input hashes match. The note SHA-256 is `beae33ee10bbffd985bdd5ec661498c84a5f53f6f2604227f5b59beedf695934`.
One analytical proof and one correction pass were used.

Evenness raises the origin zero order to \(2L+2\). The \(c_0\) jet
at \(z_*\) supplies order \(r+1\) at \(a=z_*/2\). Reality and
evenness give that order at every point in \(\{a,-a,\bar a,-\bar a\}\).
Dividing by the corresponding finite disk factors, with the
boundary bound \(\eta F(i\rho)\), gives
\[
 |\delta F(z_*)|
 \le \eta F(i\rho) (|z_*|/\rho)^{2L+2}\theta_\rho(z_*)^{r+1},
 \qquad 0<\theta_\rho(z_*)<1,\qquad \rho>|z_*|.
\]
At fixed height, disk and source tolerance, each additional \(c_0\)
derivative multiplies the same disk allowance by \(\theta_\rho(z_*)\).
The ordinary moment-series bound is a separate allowance whose
minimum with the disk bound can also be used. The growth factor
\(F(i\rho)\) remains in any comparison with increasing height.

The bound caps a centered E12 displacement disk subject to the same
source tolerance and calibrations, while each fixed E12 instance
retains positive local freedom after restricting to a positive
tolerance. This is a magnitude estimate using exact full-chain
\(c_0\) data. Acquisition of those data, a source closure with
the stated premises, and a lower Fourier or model modulus remain open.
The proof imports only the classical [maximum-modulus principle][dlmf].

[request]: VCD-E16-r1.md
[note]: ../../notes/14_VCD_E16_CALIBRATION_UPPER_BOUND_20261116.md
[dlmf]: https://dlmf.nist.gov/1.10#v
