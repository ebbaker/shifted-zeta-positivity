# Probe tail audit: a rigorous post-cutoff estimate, diagnostic finite comparison

25 September 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Model exposed: GPT-6 (Codex); exact serving variant and reasoning effort unavailable. Substantive self-audit, not independent specialist certification.

## Disposition

The revised routine's finite envelope sums are approximately $1.15683019\,10^{-12}$ and $5.58931670\,10^{-11}$, ending at block height 6063. The loop includes the block starting there, but adds no infinite remainder. Its 48-factor product, normalization and floating arithmetic are not enclosed. Thus the review erratum and reply calling the entire output a “rigorous tail bound” are too strong. The approximately $10^{-13}$ agreement is a diagnostic, not an interval-certified comparison.

The infinite remainder can be bounded separately and conservatively. The proof below gives, uniformly for $|t|\le7$,

\[
\sum_{|\gamma|\ge6063}|F(\lambda)F(-\lambda)e^{\lambda t}|
<1.665\,10^{-22},\qquad \lambda=\varrho-\tfrac12.
\tag{1}
\]

Zeros are counted with multiplicity across the full strip $0<\Re\varrho<1$. There is no extra factor 2 inside this sum: the factor for both signs is already included in the proof. The critical-line version is below $3.284\,10^{-24}$. These bounds include the *infinite* probe product. They do not certify the earlier finite block sum or the stored ordinates.

## Twelve-factor proof

Write $z=\sigma+i\gamma$, $|\sigma|\le1/2$, $a_j=2^{-j}$, and $\mathcal B(w)=\prod_j\sinh(a_jw)/(a_jw)$. For any real (x,y),

\[
\left|\frac{\sinh(x+iy)}{x+iy}\right|
\le\frac{\sinh|x|}{|x|}\le\cosh x\le e^{x^2/2}.
\tag{2}
\]

The first inequality also follows from the uniform-distribution integral; the last follows by integrating $\tanh x\le x$. For the first twelve factors use the additional bound

\[
\left|\frac{\sinh(a_jw)}{a_jw}\right|
\le\frac{\cosh(a_j\Re w)}{a_j|\gamma|}.
\]

Keep (2) for every remaining factor. Since $\sum a_j^2=1/3$ and $\prod_{j=1}^{12}a_j^{-1}=2^{78}$,

\[
|\mathcal B(1\pm z)|\le2^{78}|\gamma|^{-12}e^{3/8}.
\tag{3}
\]

Also $\mathcal B(1)\ge1$, $|1/4-z^2|\le\gamma^2+1/2$, and $|e^{zt}|\le e^{7/2}$. For $|\gamma|\ge H=6063$, the coefficient in (1) is at most

\[
C|\gamma|^{-20},\quad
C=2^{156}e^{17/4}\left(1+\frac1{2H^2}\right)^2
<2^{156}\,71\,\frac{1001}{1000}.
\tag{4}
\]

For the critical line the exponential is $e^{1/3}<7/5$ instead of $e^{17/4}<71$, with the same conservative polynomial bound.

Let $N_+(T)$ count positive ordinates with multiplicity. The classical Rosser bound

\[
\left|N_+(T)-\frac{T}{2\pi}\log\frac{T}{2\pi e}-\frac78\right|
\le0.137\log T+0.443\log\log T+1.588
\tag{5}
\]

implies $N_+(T)\le T\log T$ for $T\ge6063$. For example, bound $1/(2\pi)<1/6$, $\log\log T\le\log T$, and the remainder by $0.58\log T+2.463$; this is less than the remaining $5T\log T/6$ already for $T\ge6$. Equation (5) is recorded with constants in [Kadiri, *A zero density result for the Riemann zeta function*, equation (1.1), p. 2](https://arxiv.org/pdf/1401.4781), citing Rosser's theorem. The weaker $N_+(T)\le T\log T$ is the only counting input to (1). The current control's label “Backlund” combines constants from different historical versions; (5) suffices for the conservative estimate and is the specific bound used here.

Stieltjes integration by parts, dropping its nonpositive lower-end boundary term, gives

\[
\begin{aligned}
\sum_{|\gamma|\ge H} C|\gamma|^{-20}
&\le40C\int_H^\infty t^{-20}\log t\,dt\\
&=40C H^{-19}\left(\frac{\log H}{19}+\frac1{19^2}\right)\\
&<\frac{40\,2^{156}\,71\,(1001/1000)}{6063^{19}}
\left(\frac9{19}+\frac1{361}\right)\\
&=1.6649039728853978\ldots\,10^{-22}.
\end{aligned}
\tag{6}
\]

Using $H=6063$ deliberately overlaps the final floating block; it is conservative and removes ambiguity about the loop's last included endpoint. The decimal in (6) is only a display: the preceding rational number and its comparison with $1.665\,10^{-22}$ are checked exactly by [the standard-library control](../numerics/check_probe_postcutoff_tail.py). Its positive Taylor sums and geometric-tail bounds also prove $\log6063<9$, $e^{17/4}<71$, and $e^{1/3}<7/5$. The [small record](../numerics/records/probe-postcutoff-tail-20260925.json) records the rational numerator and denominator and the proof scope.

## What remains diagnostic, and what was changed

The earlier finite routine bounds numerator factors with a 48-factor product and divides by a floating approximation to $\mathcal B(1)^2$. The omitted infinite factors are not bounded in that routine; floating accumulation is not outward rounded. Its finite quadrature, digamma approximation, product approximation and zero ordinates also lack a combined error enclosure. Published verification that low zeros lie on the critical line does not certify the values, completeness or individual enclosures of the stored floating list. A file hash certifies file identity only.

For proportionate cleanup, the existing numerical formulas are preserved, the program's claims and field names are relabelled as finite floating envelopes, and a separately named replay record is saved. The original review and original record remain historical evidence and are superseded on certification scope by this audit. No claim of a certified error below $10^{-10}$ for the *whole comparison* is retained. The proved remainder (1) is useful, but does not turn an unenclosed finite calculation into a certificate.

Reproduce the exact remainder control with:

```sh
python3 numerics/check_probe_postcutoff_tail.py --output numerics/records/probe-postcutoff-tail-20260925.json
```

Neither physical obstruction in the [continuation note](../notes/COMPACT_RETURN_AND_PHYSICAL_TRANSLATION_SOURCES_20260925.md) uses any zero-list numerical result.
