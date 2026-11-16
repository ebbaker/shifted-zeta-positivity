# VCD-E19 r1 — canonical consumer obstruction return

16 November 2026, America/New_York. Prepared for Edward Baker with
OpenAI Codex LLM assistance. Recorded dispatch **gpt-6.1-sol / ultra**.
Separate backend model and effort attestation unavailable.

**Complete, proved in-note.** [Note 18][note] executes the frozen
[E19 r1 request][request]. All five input SHA-256 hashes matched.
The note SHA-256 is
\(\texttt{96ab576f9e19da3ad590812bf54e25fa81551a1df4ea7017ee598c376c3cf737}\).
The single correction pass clarified the initial-interval mean and
made the gamma recurrence explicit. The requested signs, limits and
consumer scope are confirmed.

The divisor expansion of \(a_n=\prod_{p\mid n}(1-p^{-2})\) gives
\(A(u)=u/\zeta(3)+C(u)\) with \(|C(u)|\le\zeta(2)+2\) for \(u\ge1\).
Partial summation gives the stated continuation of
\(Q(s)=\zeta(s)/\zeta(s+2)\) to \(\operatorname{Re}s>0,\ s\ne1\),
with remainder at most
\((\zeta(2)+2)M^{-\operatorname{Re}s}(1+|s|/\operatorname{Re}s)\)
after retaining the explicit pole term.
For fixed \(1/2<\sigma<1\) and fixed \(q\in\mathbb Q_{>0}\),
\(M=\lfloor T^2\rfloor\) gives the mean of
\(Q(\sigma+it)e^{it\log q}\) as \(a_q q^{-\sigma}\) in the limit
for integer \(q\) and zero otherwise. The pole contributes
\(O_\sigma(T^{1-2\sigma}\log T)\); the integrated remainder and
the nonmatching finite frequencies contribute
\(O_{q,\sigma}(T^{1-2\sigma})\).
Separately \(M=\lfloor |t|\rfloor\) gives
\(Q(\sigma+it)=O_\sigma(|t|^{1-\sigma})\) for \(|t|\ge2\).

For each fixed finite prime prefix \(P\), the nonnegative
weight \(\prod_{p\in P}(1+\cos(t\log p-\pi/3))\) has mean \(1\).
Its \(Q\)-weighted mean is
\(\prod_{p\in P}(1+a_p e^{-i\pi/3}/(2p^\sigma))\).
The sign of the phase is negative because the positive frequency
in the weight matches \(n^{-it}\). Elementary prime reciprocal
divergence and square summability make the product modulus tend
to infinity, with its lifted phase decreasing to \(-\infty\)
in steps tending to zero. This makes each fixed projection of the
means unbounded both ways. Positivity of the fixed weight and
vanishing of its finite initial-height contribution after averaging
force the same conclusion for each fixed projection of \(Q\) on
every tail of the vertical line. Positive and negative heights
are related by conjugation.

For each fixed \(0<y<1\), with \(s=(1+y-ix)/2\) and
\(F_\pm=F(x+i(y\pm4))\), integration by parts and the completed
zeta recurrence give, directly from the canonical source,
\[
 \frac{B(x+iy)}{4\pi F_+}
    =1-R(s)-D(s)Q(s),\qquad
 R(s)=F_-/F_+=O_y(x^{-y/2}),\qquad
 D(s)=\frac{(2s-1)(s-1)}{2(s+2)(s+1)} .
\]
Here \((D-1)Q=O_y(x^{-(1+y)/2})\), so every fixed real projection of
the normalized \(B\) and of \(DQ\) has limsup \(+\infty\) and liminf
\(-\infty\) as \(x\to+\infty\). The ratio
\(|B|/[4\pi(|F_+|-|F_-|)]\) has infinite limsup and its denominator
is positive eventually on the fixed line. Thus the proposed
uniform reverse-triangle inequality and fixed-half-plane
consumers fail on the complete canonical source at \(\lambda=0\).
The conclusions concern individual projections and height tails.
Density, effective height, simultaneous finite-observation matching,
adaptive-phase or correlated estimates, and theta zero locations
are outside their scope.

The proof uses the already checked [classical passages][refs].
The partial summation, fixed-frequency mean, prime weight and
projection argument are derived in the note. No new external
theorem or numerical evidence is used.

[request]: VCD-E19-r1.md
[note]: ../../notes/18_VCD_E19_CANONICAL_CONSUMER_OBSTRUCTION_20261116.md
[refs]: ../../references/03_CANONICAL_SCORE_FOURIER_PASSAGES_20261116.md
