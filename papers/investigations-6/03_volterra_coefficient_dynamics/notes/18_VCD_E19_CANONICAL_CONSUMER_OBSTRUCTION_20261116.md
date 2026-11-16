# VCD-E19 — failure of absolute and fixed-phase consumers on the canonical source

16 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Recorded dispatch **gpt-6.1-sol / ultra**.
Separate backend model and effort attestation unavailable.

**Proved in-note.** [E19 r1][request] executes the actual-source test
in [B05 decision11][decision11], following [decision10][decision10].
This is a scoped obstruction to two uniform consumers of the exact
canonical score at \(\lambda=0\). For each fixed \(0<y<1\), every
fixed real projection of \(B(x+iy)/(4\pi F(x+i(y+4)))\) has infinite
limsup and negative infinite liminf as \(x\to+\infty\). The absolute
ratio to the reverse-triangle margin has infinite limsup. The
classification and scope follow the [result index][results],
[coefficient cluster 18][cluster18], [control catalog 12][controls],
[avoid index][avoid], [Avoid 01][a01], [Avoid 02][a02] and
[Avoid 07][a07]. The comparison of separate absolute bounds follows
[Avoid 12][a12].

## 1. Summatory coefficients and continuation

Put \(Q(s)=\zeta(s)/\zeta(s+2)\) and
\(a_n=\prod_{p\mid n}(1-p^{-2})\), with \(a_1=1\).
The divisor expansion is \(a_n=\sum_{d\mid n}\mu(d)d^{-2}\), where
\(\mu(d)\) is the Möbius function. In \(\operatorname{Re}s>1\),
both factors in
\[
 \sum_{n\ge1}a_n n^{-s}
 =\left(\sum_{m\ge1}m^{-s}\right)
   \left(\sum_{d\ge1}\mu(d)d^{-s-2}\right)=Q(s)
\]
converge absolutely. The reciprocal series follows by expanding the
Euler product in \(\operatorname{Re}(s+2)>1\). Likewise
\(c=\sum_{d\ge1}\mu(d)d^{-3}=1/\zeta(3)\). The Euler product
also gives nonvanishing of \(\zeta(s+2)\) for \(\operatorname{Re}s>0\).
[Checked classical formulas][refs]

For \(u\ge1\) write \(A(u)=\sum_{n\le u}a_n\) and \(C(u)=A(u)-cu\).
The divisor expansion gives
\[
 \begin{aligned}
 A(u)
 &=\sum_{d\le u}\frac{\mu(d)}{d^2}\left\lfloor\frac ud\right\rfloor\\
 &=u\sum_{d\le u}\frac{\mu(d)}{d^3}+O\left(\sum_{d\le u}d^{-2}\right)
   =cu+O(1).
 \end{aligned}
\]
In fact \(|C(u)|\le K:=\zeta(2)+2\), since
\(u\sum_{d>u}d^{-3}\le u/(2\lfloor u\rfloor^2)\le2\) and the
rounding error is at most \(\zeta(2)\).

For an integer \(M\ge1\), partial summation on \(M<n\le X\) gives
\[
 \sum_{M<n\le X}a_n n^{-s}
  =A(X)X^{-s}-A(M)M^{-s}
    +s\int_M^X A(u)u^{-s-1}\,du .
\]
First let \(X\to\infty\) in \(\operatorname{Re}s>1\), where the upper
endpoint vanishes. Substituting \(A(u)=cu+C(u)\) yields
\[
 \begin{aligned}
 Q(s)&=\sum_{n\le M}a_n n^{-s}
       +\frac{c M^{1-s}}{s-1}+\mathcal R_M(s),\\
 \mathcal R_M(s)&=-C(M)M^{-s}+s\int_M^\infty C(u)u^{-s-1}\,du .
 \end{aligned} \tag{1}
\]
For \(\rho=\operatorname{Re}s>0\), the remainder satisfies
\[
 |\mathcal R_M(s)|\le K M^{-\rho}(1+|s|/\rho). \tag{2}
\]
The integral converges locally uniformly on \(\rho>0\), by domination
on each compact subset with real parts bounded below by a positive
constant. Its holomorphy and the identity theorem extend (1) to
\(\rho>0,\ s\ne1\).

## 2. Fixed rational frequencies and a pointwise bound

Fix \(1/2<\sigma<1\) and \(q\in\mathbb Q_{>0}\). For \(T\ge2\) take
\(M=\lfloor T^2\rfloor\), held constant over \(0\le t\le T\).
Multiply (1) on \(s=\sigma+it\) by \(e^{it\log q}\) and average.
The pole term has averaged absolute value at most
\[
 \frac{c M^{1-\sigma}}{T}\int_0^T
      \frac{dt}{\sqrt{(1-\sigma)^2+t^2}}
   =O_\sigma(T^{1-2\sigma}\log T).
\]
By (2) the averaged absolute remainder is
\(O_\sigma(M^{-\sigma}(1+T))=O_\sigma(T^{1-2\sigma})\).

The frequency for \(n\) in the finite sum is \(\log(q/n)\).
When \(q\) is an integer and \(M\ge q\), the zero frequency contributes
\(a_q q^{-\sigma}\). Every other averaged exponential has modulus
at most \(2/(T|\log(q/n)|)\). The terms \(n\le2q\) with \(n\ne q\)
give \(O_{q,\sigma}(T^{-1})\) because their set is fixed and finite.
For \(n>2q\) the logarithm has modulus at least \(\log2\), and
\(0<a_n\le1\) gives the bound
\[
 \frac{2}{T\log2}\sum_{n\le M}n^{-\sigma}
   =O_\sigma(T^{-1}M^{1-\sigma})
   =O_\sigma(T^{1-2\sigma}).
\]
Since \(1-2\sigma<0\), the three errors vanish and
\[
 \lim_{T\to\infty}\frac1T\int_0^T Q(\sigma+it)e^{it\log q}\,dt
  = \begin{cases}
       a_q q^{-\sigma}, & q\in\mathbb N,\\
       0, & q\notin\mathbb N .
    \end{cases} \tag{3}
\]
Constants here can depend on the fixed \(q\) and \(\sigma\).

For a separate pointwise bound, take \(M=\lfloor t\rfloor\) for
\(t\ge2\). The finite sum in (1) has modulus at most
\(\sum_{n\le M}n^{-\sigma}=O_\sigma(t^{1-\sigma})\). The pole term
is \(O_\sigma(t^{-\sigma})\) by \(|\sigma+it-1|\ge t\), and
(2) is \(O_\sigma(t^{1-\sigma})\). Therefore
\[
 |Q(\sigma+it)|=O_\sigma(t^{1-\sigma}). \tag{4}
\]
All data in (1) are real on the real axis, so (1) also gives
\(Q(\bar s)=\overline{Q(s)}\). The same bound holds for negative heights
with \(|t|\ge2\).

## 3. Nonnegative prime weights and unbounded projections

Take \(\alpha=\pi/3\) and let \(P\) be a fixed finite prefix of
the increasing sequence of primes. Define
\[
 W_P(t)=\prod_{p\in P}\bigl(1+\cos(t\log p-\alpha)\bigr)\ge0 .
\]
Its frequencies are \(\log q\), where \(q=\prod_{p\in P}p^{k_p}\)
for \(k_p\in\{-1,0,1\}\). The coefficient for \(k_p=1\) is
\(e^{-i\alpha}/2\), for \(k_p=-1\) it is \(e^{i\alpha}/2\), and
for \(k_p=0\) it is \(1\). By unique factorization only the all-zero
choice gives \(q=1\). All other ordinary exponential means vanish,
so \(\lim_{T\to\infty}T^{-1}\int_0^T W_P(t)\,dt=1\).
To average \(QW_P\), apply (3) to this finite frequency set.
The surviving integer \(q\) have all \(k_p\ge0\) and are squarefree.
On these choices \(a_q=\prod_{k_p=1}(1-p^{-2})\). Thus
\[
 \lim_{T\to\infty}\frac1T\int_0^T Q(\sigma+it)W_P(t)\,dt
   =L_P:=\prod_{p\in P}\left(1+\frac{a_p e^{-i\alpha}}{2p^\sigma}\right).
 \tag{5}
\]
Both height means take \(T\to\infty\) for each fixed \(P\).

Set \(h_p=a_p/(2p^\sigma)\). The inequalities
\(a_p\ge3/4\), \(\sigma<1\) and \(2\sigma>1\) give
\[
 \sum_p h_p\ \ge\ \tfrac38\sum_p p^{-1}=\infty,\qquad
 \sum_p h_p^2\ \le\ \tfrac14\sum_{n\ge2}n^{-2\sigma}<\infty .
\]
For the prime reciprocal divergence, unique factorization gives
\(\sum_{n\le N}n^{-1}\le\prod_{p\le N}(1-p^{-1})^{-1}\) by expanding
the finite product of geometric series. The logarithm of the product
is at most \(2\sum_{p\le N}p^{-1}\) because
\(-\log(1-v)\le2v\) for \(0\le v\le1/2\). The harmonic sum
diverges, forcing the prime reciprocal sum to diverge as well.

Each factor of \(L_P\) lies in the open right half-plane and has
negative imaginary part. Use its logarithm continued from \(1\)
along the segment \(1+u h_p e^{-i\alpha}\), \(0\le u\le1\).
Since \(0<h_p<1/2\), the Taylor series gives
\(\log(1+h_pe^{-i\alpha})=h_pe^{-i\alpha}+O(h_p^2)\) with an
absolute implied constant. For increasing prime prefixes this gives
\[
 \log |L_P|=\cos\alpha\sum_{p\in P}h_p+O(1)\longrightarrow+\infty,
 \qquad
 \Theta_P:=\sum_{p\in P}\arg(1+h_pe^{-i\alpha})
      =-\sin\alpha\sum_{p\in P}h_p+O(1)\longrightarrow-\infty .
\]
The lift \(\Theta_P\) decreases strictly and its steps tend to zero.
For any fixed real \(\phi\), choose the first prefix crossing each
target \(\phi-2\pi k\) for positive integers \(k\) sufficiently large.
The crossing indices tend to infinity and their overshoots are
bounded by the last phase step, hence tend to zero. The corresponding
\(\cos(\Theta_P-\phi)\) tends to \(1\).
For the targets \(\phi+\pi-2\pi k\) the same construction yields
cosine tending to \(-1\). Since \(|L_P|\to\infty\), the values
\(\operatorname{Re}(e^{-i\phi}L_P)\) are arbitrarily large both
positively and negatively.

Let \(U_\phi(t)=\operatorname{Re}(e^{-i\phi}Q(\sigma+it))\).
If \(U_\phi(t)\le H\) for every \(t\ge t_0\), then for each fixed
\(P\),
\[
 \frac1T\int_0^T U_\phi(t)W_P(t)\,dt
   \le \frac1T\int_0^{t_0}U_\phi(t)W_P(t)\,dt
       +\frac H T\int_{t_0}^T W_P(t)\,dt .
\]
The first integral has a finite numerator because \(Q\) is regular
on the line and \(W_P\) is continuous and bounded for fixed \(P\).
Likewise the initial portion of the mean of \(W_P\) vanishes.
Equations (5) and the weight mean would give
\(\operatorname{Re}(e^{-i\phi}L_P)\le H\) for every prefix, which
contradicts the positive crossings. Applying the same argument to
\(-U_\phi\) and the negative crossings proves
\[
 \limsup_{t\to+\infty}\operatorname{Re}(e^{-i\phi}Q(\sigma+it))=+\infty,
 \qquad
 \liminf_{t\to+\infty}\operatorname{Re}(e^{-i\phi}Q(\sigma+it))=-\infty .
 \tag{6}
\]
In particular, for every fixed \(\sigma,\phi\), every \(H>0\), and
every initial height, there are actual heights beyond it at which
the projection exceeds \(H\) and falls below \(-H\), respectively.
Conjugation gives the corresponding statement as \(t\to-\infty\).
These are unbounded projections. Density, effective heights,
simultaneous matching of a finite list of observations, and zeros
are outside this conclusion. The proof uses no universality theorem
and makes no novelty claim for positive trigonometric weighting or
Dirichlet-series value distribution.

## 4. Exact transfer to the canonical remainder

At \(\lambda=0\) the [manuscript][manuscript] gives the complete
positive even source \(\Phi\), \(Z=\int_{\mathbb R}\Phi\), and
\[
 F(z)=\frac1Z\int_{\mathbb R}\Phi(u)e^{izu}\,du
     =\frac{\xi(s)}{4Z},\qquad s=(1-iz)/2.
\]
Use the [E06][e06] remainder \(b(u)=-\Phi'(u)/\Phi(u)-8\pi\sinh(4u)\)
and \(B(z)=Z^{-1}\int_{\mathbb R} b(u)\Phi(u)e^{izu}\,du\).
The double-exponential bounds on \(\Phi,\Phi'\) justify integration
by parts and give vanishing endpoints for every fixed \(z\).
Writing \(F_\pm=F(z\pm4i)\), the terms \(e^{4u}\) and \(e^{-4u}\)
shift \(z\) to \(z-4i\) and \(z+4i\), respectively. Thus
\[
 B(z)+4\pi(F_- -F_+)
  =-\frac1Z\int_{\mathbb R}\Phi'(u)e^{izu}\,du
  =izF(z). \tag{7}
\]

Fix \(0<y<1\), put \(z=x+iy\), and set
\(\sigma=(1+y)/2\), so \(s=\sigma-ix/2\).
The shifted \(\xi\) arguments are \(s+2\) and \(s-2\).
By reflection, the latter can be replaced by \(3-s\).
The exterior real parts are \(\sigma+2\) and \(3-\sigma\), both
greater than \(2\). For a fixed exterior real part \(a>1\),
the Euler product gives
\(\prod_p(1+p^{-a})^{-1}\le|\zeta(a+it)|\le\zeta(a)\).
In particular the exterior factors are bounded above and bounded
away from zero, and \(F_+\) is nonzero since its remaining
completion factors are nonzero. In
\(\xi(w)=w(w-1)\pi^{-w/2}\Gamma(w/2)\zeta(w)/2\),
vertical Stirling for \(\Gamma(w/2)\) gives its magnitude
comparable to \(x^{\operatorname{Re}w/2-1/2}e^{-\pi x/8}\)
at the two exterior arguments as \(x\to+\infty\).
The polynomial has modulus comparable to \(x^2\) at both, and
the exponential factors cancel in their ratio. Consequently
\[
 R(s):=\frac{F_-}{F_+}=\frac{\xi(3-s)}{\xi(s+2)}
       =O_y\left(x^{(1-2\sigma)/2}\right)=O_y(x^{-y/2}).
\]
[Checked Euler product, reflection and Stirling formulas][refs]

Using \(\Gamma((s+2)/2)=(s/2)\Gamma(s/2)\) in the completion gives
\[
 \frac{F(z)}{F_+}
 =\frac{\xi(s)}{\xi(s+2)}
 =\frac{2\pi(s-1)}{(s+2)(s+1)}Q(s).
\]
As \(iz=1-2s\), (7) therefore gives
\[
 \mathcal B_y(x):=\frac{B(x+iy)}{4\pi F_+}
    =1-R(s)-D(s)Q(s),\qquad
 D(s)=\frac{(2s-1)(s-1)}{2(s+2)(s+1)} . \tag{8}
\]
The difference \(D(s)-1=-(9s+3)/(2(s+2)(s+1))\) is \(O_y(x^{-1})\).
Equation (4) at \(t=-x/2\) gives
\((D(s)-1)Q(s)=O_y(x^{-\sigma})\). Thus (8) becomes
\(\mathcal B_y(x)=1-Q(\sigma-ix/2)+o_y(1)\). By (6) and conjugation,
for every fixed \(y\in(0,1)\) and \(\phi\in\mathbb R\),
\[
 \limsup_{x\to+\infty}\operatorname{Re}(e^{-i\phi}\mathcal B_y(x))
    =+\infty,\qquad
 \liminf_{x\to+\infty}\operatorname{Re}(e^{-i\phi}\mathcal B_y(x))
    =-\infty . \tag{9}
\]
Equation (4) also shows directly that \(D(s)Q(s)\) has the same
unbounded projections as \(Q(s)\). As \(1-|R(s)|\to1\), the
denominator below is eventually positive and (9) gives
\[
 \limsup_{x\to+\infty}
 \frac{|B(x+iy)|}{4\pi(|F_+|-|F_-|)}
 =\limsup_{x\to+\infty}\frac{|\mathcal B_y(x)|}{1-|R(s)|}
 =+\infty . \tag{10}
\]

## 5. Consumer scope and control premises

The sufficient pointwise inequality
\(|B|<4\pi(|F_+|-|F_-|)\) in [decision10][decision10] fails at
arbitrarily large heights on every fixed line \(0<y<1\), even as
a non-strict inequality. Its ratio exceeds each fixed comparison
constant at arbitrarily large heights. By (9), any fixed affine
half-plane restriction on \(B/(4\pi F_+)\) or \(D(s)Q(s)\) fails on
every height tail of the same line. The defining normal and threshold
of the half-plane may depend on the fixed \(y\). The obstruction
concerns those uniform-in-height consumers at \(\lambda=0\).
Height-dependent phases, correlated estimates and bounds on selected
subregions have separate hypotheses. The result gives no confinement
or nonreal-zero conclusion for theta.

The proof uses the actual source as the witness. For the
[catalog][controls] comparison, the premise under test is the
unchanged complete canonical score and the literal Fourier readout
with the \(\xi\) evaluation in (7)–(8).

| Recorded control class | Premise missing from this test |
| --- | --- |
| Euler-factor translates | The literal transform has a further finite Euler multiplier, so the exact canonical \(\xi\) evaluation fails and the score changes. |
| Weighted-square controls and finite-source measurements | The complete equal-coefficient square expansion changes, and a nonzero finite square change loses full canonical reflection. The finite-source zero theorem concerns that class. |
| Reflected super-Gaussian | Evenness survives, while the canonical arithmetic expansion and the bounded exponential-reference score remainder fail. |
| Smooth shape and positive-primitive controls | The complete equal-coefficient square expansion and literal \(\xi\) Fourier evaluation are absent, including when the primitive asymptotic coefficients survive. |
| Finite-prime orbit controls | These change canonical square coefficients and lose full reflection despite retaining the prescribed finite arithmetic identities. |
| Fixed-event atoms and finite-profile controls | Atoms lack the required smooth positive density. Compact triangular extensions lack positive full-line density and the canonical arithmetic evaluation. |
| RH-conditional normalized endpoint controls | Ordinary Dirichlet-series arithmetic fails even under their stated RH hypothesis. |
| Fixed amplitude with variable observation kernel | The unchanged source survives, while the literal exponential observation in (7)–(8) fails. |
| Actual-theta finite-profile relaxation | The relaxed measure represents finite profile data without supplying the corresponding physical source and Fourier readout. |

The [E07/E10/E12 source screens][midpoint] similarly retain selected
canonical score observations while changing source coefficients or
the actual pointwise score. Each retains its own zero scope.
These premise comparisons preserve the separation recorded in
[decision11][decision11]. The present failure follows from the
full canonical arithmetic itself.

[request]: ../research-progress/handoffs/VCD-E19-r1.md
[decision10]: ../brainstorm/notes/10_VCD_B05_CANONICAL_FOURIER_SCORE_DECISION_20261116.md
[decision11]: ../brainstorm/notes/11_VCD_B05_CANONICAL_CONSUMER_TEST_DECISION_20261116.md
[refs]: ../references/03_CANONICAL_SCORE_FOURIER_PASSAGES_20261116.md
[e06]: 06_VCD_E06_EXPONENTIAL_SCORE_RESIDUAL_20261116.md
[midpoint]: 15_VCD_MIDPOINT_RESEARCH_SYNTHESIS_20261116.md#2-finite-canonical-score-and-midpoint-data-leave-local-freedom
[manuscript]: ../manuscript/main.tex
[results]: ../../../../result-summaries/README.md
[cluster18]: ../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
