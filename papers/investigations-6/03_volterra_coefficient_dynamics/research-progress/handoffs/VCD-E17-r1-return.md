# VCD-E17 r1 — Complete canonical remainder contour return

16 November 2026, America/New_York. Prepared for Edward Baker with
OpenAI Codex LLM assistance. Recorded task dispatch **gpt-6.1-sol / ultra**.
Separate runtime configuration or backend attestation unavailable.

**Complete, proved in-note.** [Note 16][note] executes [E17 r1][request].
All five pinned input hashes match. Note SHA-256 is
\(\texttt{a1d05faa121e368f656a2a277d60b61e0ca4018213c0cf5142d155cb060d0f66}\).
One analytical proof and one correction pass were used.

The complete square-mode expansion of \(g=b\Phi\) cancels the first
cubic mode before taking moduli. Its derivative/product definition
and inherited theta reflection give a holomorphic odd continuation
to \(|\operatorname{Im}u|<\pi/8\). Uniform double-exponential decay on
closed substrips justifies the contour shift and the stated
\(|B(x+iy)|\le e^{-v|x|} A_Y(\cos(4v))\) estimate.

A lattice Riemann sum with an integrable dominating function proves
\(A_Y(\delta)\sim15\delta^{-7/2}/[Z(1-Y)]\) for each fixed \(0\le Y<1\).
Optimizing over \(v\) gives the frozen constant and power
\[
\inf_{0\le v<\pi/8}e^{-vX} A_Y(\cos(4v))
\sim \frac{15}{Z(1-Y)}\left(\frac{eX}{14}\right)^{7/2}e^{-\pi X/8}.
\]
No correction to either frozen formula was required. The correction
pass clarified the control premises. The note records that the
fixed-contour allowance is finite even at \(Y=1\), where
\(\delta^{7/2}A_1(\delta)\to+\infty\). Both displayed asymptotics have
fixed-\(Y\) scope and are nonuniform as \(Y\uparrow1\).

The optimized asymptotic measures the displayed termwise allowance.
It gives an upper bound on the magnitude of the canonical transform
and leaves open stronger cancellation-aware estimates. The control
screen distinguishes the own score of a perturbation from testing
the canonical symbol on its density. No fresh external reference
was used. E18 owns the comparison with the exterior anchors.

[request]: VCD-E17-r1.md
[note]: ../../notes/16_VCD_E17_CANONICAL_REMAINDER_CONTOUR_BOUND_20261116.md
