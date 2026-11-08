# E21 r1: assessment of the paid comparison and scoped Euler obstructions

7 November 2026 UTC. Prepared for **Edward Baker** with substantial OpenAI Codex assistance. Assessor explicitly tool-selected **gpt-6.1-sol, reasoning effort ultra**, in a separate worker from the E20 executor. This records the supplied actual tool selection, not independent backend verification. Conceptual lead selected gpt-6-astra/ultra; root configuration unavailable. Shared premises and the same model family prevent a claim of independent specialist assessment.

**Disposition: accepted within the exact scope of request38, with no correction to the assessed sources.** One bounded internal correction to this review's future-routing wording is recorded in §6. [Note28](../notes/28_TND_O_E20_PAID_QUADRATIC_GREEN_COMPARISON_20261107.md) supplies its paid quadratic Green comparison, complete-boundary acquisition payments and fixed-Q averaged obstruction. [Note29](../notes/29_TND_O_E20_R2_UNIFORM_EULER_LENGTH_OBSTRUCTION_20261107.md) supplies the stated uniform growing-length obstruction. This assessment **explicitly includes mechanism2 in Decision17 §6**, with its actual Euler-control premises and restricted information class. None of these results acquires favorable canonical signed smallness, proves canonical nonreal zeros, or excludes them.

## 1. Contract, versions and assessment boundary

[Request38](../research-progress/handoffs/38_TND_O_E21_SIGNED_ACQUISITION_ASSESSMENT_REQUEST_20261107.md) fixes this Type E task. All **59** sources in [inputs38](../research-progress/handoffs/38_TND_O_E21_SIGNED_ACQUISITION_ASSESSMENT_INPUTS_20261107.json) matched their byte counts and SHA-256 hashes before substantive assessment and again at return. Inputs38 itself is 15,502 bytes, SHA-256 `be5cf86bf2081ec6959a5e9d95fd63bc9a8a32b3ecfcb7e491a4e6499995795d`. The frozen request and all mathematical sources remained unchanged. Hashes establish version identity, not correctness.

The actual claims in Notes28–29 and Decision17 were audited against the inherited normalization, complete-source majorant, accepted Green identity and prime baseline. Earlier manuscript theorems and E16/E17/E19 are inherited inputs, not newly independently proved here. The root policies, model workflow, [result index](../../../../../result-summaries/README.md), [controls12](../../../../../result-summaries/12_collision_controls_and_screening.md), [pattern index](../../../../../avoid/README.md), [target rule01](../../../../../avoid/01_restating_the_target.md), [control rule02](../../../../../avoid/02_shape_only_arguments_and_the_controls.md), [shared-premise rule05](../../../../../avoid/05_same_model_reviews_and_shared_premises.md) and [scope rule07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md) retain their meanings. An RH-equivalent vanishing requirement is not counted as newly acquired sign information.

One targeted read-only supplement checked the existing Euler family in its original manuscript, specifically Lemma `lem:kernel`, Proposition `prop:arith`, and the S1–S5/D1–D3 screening passages:

`/Users/ebbaker/Documents/shifted-zeta-positivity/papers/investigations-2/active/19_euler_factor_controls/manuscript/euler_factor_controls.tex`

It is **53,664 bytes**, SHA-256 `eb6ac32cef893ce60cd29835054a6769ca483622e0a1514716cac12800242f38`. This is a separately recorded supplementary reading, **not one of the initial 59 frozen sources**; inputs38 was not rewritten. Only those passages were needed. No compile, numerical witness, full inherited-proof audit or amendment of that manuscript was undertaken.

The assessor directly opened BCR v1's primary converted text and DLMF 5.8.2; their exact uses are below. No PDF possession, full-paper proof audit, literature novelty assessment, numerical research or subdelegation is claimed. Only this review and return38 were written. Root owns shared files and research-chat capture.

## 2. Note28: analytic normalization and quadratic comparison

The coordinate \(s=1/2-iz/2\) sends heights \(0,4,8\) to real parts \(1/2,5/2,9/2\). Xi reflection leaves the supplied normalization \(H_0=\xi(s)/8\) unchanged. With \(a=\pi/8\), \(K(u)=(16\cosh au)^{-1}\), each horizontal line has mass \(\pi/(16a)=1/2\); their union is a probability measure. Scalar cancellation and all variance/Jensen factors therefore have the correct normalization.

Fractional-part continuation in Note28(8) follows from partial summation for \(\Re s>1\), followed by holomorphic continuation of its integral to \(\Re s>0\). In particular \(q\zeta=1-(s-1)\int_1^\infty\{v\}v^{-s-1}dv\) is analytic through \(s=1\), with value one. Thus \(F_Q(i)=M_Q(1)\ne0\). The pole at \(s=0\) is outside the closed strip, and \(1-p^{-s}\ne0\) there. The lower-strip zeta pole is neither retained nor turned into an artificial zero.

The uniform bound \( |q\zeta|\le8+|x| \) on the whole closed strip, multiplied by the finite \(C_Q\), is enough for the real and imaginary strip Poisson formulas. Vertical-side harmonic measure decays exponentially, so polynomial horizontal growth leaves no side contribution. The resulting mean is the **complex** identity \(\int F_Qd\mu_X=c_Q(X)\). Merely averaging moduli would not suffice for the subsequent variance identity.

On the center line, \(3/5\le|q|\le1\), and the remaining absolutely convergent Euler product lies between the products of \((1+p^{-5/2})^{-1}\) and \((1-p^{-5/2})^{-1}\). Including all primes weakens these bounds to \(\zeta(5)/\zeta(5/2)\) and \(\zeta(5/2)\), respectively. Thus the stated \(c_0,U_0\) are positive and uniform in all real \(X\) and finite \(Q\).

The exact quotient is

\[
 D_Q=\frac{F_Q}{H_0}
 =\frac{16\pi^{s/2}M_Q(s)}{s^2\Gamma(s/2)}.
\]

The factor 16 agrees with \(H_0=\xi/8\) and \(\xi=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta\). This quotient is analytic and zero-free on a neighborhood of the closed strip. Its log modulus has at most linear-plus-logarithmic growth, so the same Poisson limit proves its zero Green functional. The inherited complete logarithmic integrability handles real boundary zeros with their true multiplicities. Consequently Note28(12) equals the canonical \(J_0\) exactly. There is **no additional** \(G(X,1)\) to attach to this pole-cancelled representation; the separate prime-baseline formula already has its own correct plus pole term.

Expansion of the square using the complex mean gives

\[
 1+\epsilon_Q^2=\int |F_Q/c_Q|^2d\mu_X.
\]

All terms are integrable by the polynomial field bound. Jensen applied to this square gives \(J_0\le\tfrac12\log(1+\epsilon_Q^2)\), while \(J_0\ge0\) comes from the inherited positive complete Green sum. Boundary zeros have measure zero and integrable logarithms, so Jensen introduces no missing singular term. For \(0<d\le1\), \(\operatorname{atanh}v\ge v\) and \(\sin(ay)\ge y\sin a\) give exactly \(m(d,r)=\sin(a)d/\cosh(ar)\). Thus the strict threshold \(\epsilon_Q^2<e^{2m}-1\) is sufficient for the declared one-defect exclusion. No part of this calculation asserts its hypothesis.

## 3. Note28: complete acquisition and order of limits

The source majorant is the literal complete reflected theta source. The half-Fourier factor is \(1/2\); the coefficient sum of \(P_0=2v^2-3v\) is five. Splitting omitted arithmetic terms on \(|u|\le U\) from the **complete** radial tail outside that interval gives exactly Note28(15). Reflection of a finite prefix is used only inside an undifferentiated integral. It does not acquire the complete source's odd derivative matching at zero.

The compact conversion factor \(B_Q(X,R)\) is the actual supremum of \(D_Q\) on the two finite boundary segments. The rough replacement in (17) follows from \(|s|\ge1/2\), \(\Re s\le9/2\) and \(|M_Q|\le C_Q\). The supplementary closed bound (17a) also checks: [DLMF 5.8.2](https://dlmf.nist.gov/5.8#E2) gives the reciprocal-gamma product; applying \(\log|1+v|\le\Re v+|v|^2/2\) to its factors gives \(|\Gamma(w)^{-1}|\le|w|e^{\gamma\Re w+\pi^2|w|^2/12}\). With \(w=s/2\), \(\gamma\le1\), \(1/(2|s|)\le1\), and \(|s|^2\le(81+(|X|+R)^2)/4\), this is precisely the displayed conservative exponential. It is expensive but finite; it supplies no uniform full-line gamma bound.

The restricted probability mass is \(\mu_R=(2/\pi)\arctan(\sinh(aR))\le1\). Hence the source norm error is at most \(B_Q\delta_H/c_0\), with no extra boundary or square-root factor. It is deliberately applied only on the compact segments.

Both remote boundaries are paid using the **exact** canonical field: the lower-boundary estimate is \(C_Q(2+|x|)\), and the upper-boundary estimate is \(\zeta(9/2)\). For \(u=|x-X|\), \(K\le e^{-au}/8\) and \(|v-1|^2\le2|v|^2+2\). Summing two directions and both boundary lines gives

\[
 \frac12\int_R^\infty e^{-au}
 \left[\frac{C_Q^2}{c_0^2}(2+|X|+u)^2+
       \frac{\zeta(9/2)^2}{c_0^2}+2\right]du.
\]

Integrating this polynomial yields exactly \(\tau_Q\) in (21). The factors require no correction. Compact triangle inequality and the remote square norm give (22), without assigning the finite-source approximation any unproved remote behavior.

The safe denominator uses precisely primes \(p>Q\) and integer-cutoff powers \(p^k\le L\). Each omitted log coefficient is at most one, so the integral-test tail is \(2L^{-3/2}/3\). Exponentiation gives \(\eta_L=U_0(e^{\beta_L}-1)\), uniformly in phase; (25) solves this allowance correctly. A later finite-arithmetic error must be added.

For a general center error \(|c-\widetilde c|\le\eta\), the declared \(\ell=|\widetilde c|-\eta>0\) gives the exact denominator propagation (26) and hence (27). The known lower bound \(c_0\le|c|\) may also be used directly. In §6, choosing \(\eta<c_0/4\) ensures \(|\widetilde c|>3c_0/4\); the actual denominator difference is therefore at most \( (4/3)\eta\|\widehat F_Q\|/c_0^2\), and the stated conservative factor two is valid. This check does not require replacing the known \(|c|\) bound by the weaker \(\ell\).

The prescribed order is valid: first \(R\) for the exact remote tail, then \(N,U\) with the now fixed finite compact amplification, then denominator precision. The bound on \(\|\widehat F_Q\|\) follows from positivity of the undifferentiated reflected prefix and the complete \(B_0J/2\) majorant. Every step terminates for each finite parameter tuple and positive budget. Repeating it along a specified varying-parameter sequence does not interchange limits through an unbounded gamma factor.

The remaining compact field integrals and residual norms are exact, unevaluated objects. Later quadrature and rounding need their own payments. The result supplies arbitrarily accurate pointwise acquisition at arbitrary finite height, **not** uniform computational cost, a uniform residual bound, coverage of all centers, or smallness as \(d\downarrow0\). The text preserves these distinctions.

## 4. BCR use and both moment obstructions

The assessor directly checked [arXiv:1411.7764v1](https://arxiv.org/html/1411.7764v1), §1, (1.1), the polynomial hypothesis and Theorem 1. The pinned version is dated 28 November 2014; the converted text's anomalous August 2026 date is not a version change. The imported statement uses a fixed smooth weight supported in \([1,2]\), arbitrary coefficients \(a_n\ll n^\varepsilon\), length \(N=S^\theta\), \(\theta<17/33\), the stated gcd/lcm logarithmic main term, and remainder \(O(S^{3/20+\varepsilon}N^{33/20}+S^{1/3+\varepsilon})\). The targeted proof passages around (3.7) and §3.3 support dependence on coefficient bounds rather than on a special support pattern. This is a uniformity check, not a full proof audit.

For the bounded class \(|a_n|\le1\), every coefficient-growth seminorm has common bound one. Fresh theorem applications thus have constants depending on the fixed weight, exponent and error allowance, not on \(Q\) or a changing divisor support. No numerical BCR constant or computable threshold was extracted. The source does not explicitly list such numerical constants, and the notes correctly refrain from declaring them intrinsically ineffective.

For fixed \(Q\), Note28 pads the actual length \(P_Q\) to \(S^{1/4}\) once \(S\ge P_Q^4\). The remainder exponent \(3/20+33/80=9/16\) is correct. The leading coefficient is \(\kappa_Q=\prod_{p\le Q}(1-1/p)>0\); each local sum is \(1-1/p-1/p+1/p\). All remaining logarithmic constants are finite for fixed \(Q\). This proves the stated \(\kappa_Q S\log S\int\phi+O_{Q,\phi}(S)\), with no growing-\(Q\) conclusion borrowed from it.

Note29 instead applies the theorem afresh to the common bounded coefficient class at \(N=S^\theta\). Its full gcd-log sign checks directly: the logarithm vanishes when a prime divides both or neither index; in each mixed case the weight is \(-1/p\) and the logarithm is \(-\log p\). The two mixed products are positive. Summing all other prime states gives exactly

\[
 2\kappa_Q\sum_{p\le Q}\frac{\log p}{p-1}.
\]

It is therefore legitimate to drop that correction for a lower bound. After \(t=Su\), the constant term is bounded below by \(-B_\phi\) because \(0<\kappa_Q\le1\); no \(Q\)-dependent negative term is concealed in an error.

The elementary coefficient estimate in Note29(13)–(17) is valid for any finite prime set. Adding every odd composite factor below \(y\) only lowers the product, so the selected small-prime product is at least \(\tfrac12\prod_{j\le m}2j/(2j+1)\). The induction inequality has difference one, and gives \(1/(2\sqrt y)\). For the remaining primes, their number is at most \(\log L/\log y\) and \(-\log(1-1/p)\le2/p\le2/y\). With \(y=\max(3,\log L)\), their total logarithmic loss is at most \(2/\log3\). Thus the displayed lower bound needs neither PNT nor a missing prime-density input. When \(\log S\ge3/\theta\), it gives the uniform \(\sqrt{\log S}\) main term claimed.

The explicit \(\varepsilon_\theta=\tfrac12\min((17-33\theta)/20,2/3)\) leaves both error exponents strictly negative after division by \(S\). Bounding the decaying terms by \(2C_{\rm BCR}\) for \(S\ge1\) is conservative and \(Q\)-independent. The constants and threshold in (24)–(25) have exactly the permitted dependence.

Both notes use the **complete nonnegative convolution**, justified by Tonelli. On the lower boundary \(|q(1/2-ix/2)|=1\); conjugation changes no square modulus. On \(x\in[T+1,2T-1]\), the center mass is at least \(k_1=\pi^{-1}\arctan(\sinh(\pi/8))\). The fixed support separation of \(\phi\) supplies the stated trimming threshold. Dropping the nonnegative top-boundary square and using \(|c|\le U_0\) has the correct lower-bound direction. Finally \(x=2t\), \(S=T/2\) gives \(dx=2dt\) and \(2S=T\), leaving no extra factor of two.

Thus Note28(36)'s fixed-\(Q\) logarithmic coefficient is correct. Note29(26) actually proves twice its conservatively stated coefficient in (5); retaining half causes no problem. Its \(C_{\theta,\phi}\) and \(T_{\theta,\phi}\) are independent of every admissible \(Q\), with unspecified imported BCR constants honestly retained.

The conclusion concerns \(\epsilon_Q^2\), not \(J_0\). It excludes uniform all-center bounded residuals for fixed finite \(Q\), and for \(P_Q\le(T/2)^\theta\) with fixed \(0<\theta<17/33\) and one \(Q\) on each averaging interval. It does not imply a large residual at every center, an exceptional-set bound, a large Green potential, or canonical nonreal zeros. Adaptive (Q(X)), longer products and arbitrary preconditioners are outside this theorem.

## 5. Decision17 §6: actual safe-line control instability

This mechanism is explicitly assessed here. For \(0<d<1\), \(\beta=(1+d)/2<1\), the two factored terms of \(D_p\) give (6.2)–(6.3) uniformly on each fixed \(\Re s\ge\sigma_0>1\). Logarithmic derivative factors do not defeat the negative prime powers at any fixed jet order. Absolute Dirichlet-series bounds for the fixed safe half-plane then give the same convergence for the stated zeta jets. Multiplication by \(D_p\) changes no Dirichlet coefficient \(n<p\), and changes only the Euler factor at \(p\).

The completion calculation is exact:

\[
 p^{s-1/2}D_p(s)
 =2\cos(a_pz)+2\cosh(d\log p/2).
\]

Dividing by the second term produces \(1+c_p\cos(a_pz)\), with \(c_p=\operatorname{sech}(d\log p/2)\in(0,1)\). This is precisely the existing positive even-source Euler family with \(a_p=\log p/2\). The source translations, positivity, full even reflection, all fixed exponential moments and actual heat orbit follow for each fixed \(p\); uniform source constants in \(p\) are not supplied.

The added simple zeros are exactly \(x_k\pm id\), \(x_k=2(2k+1)\pi/\log p\), of spacing \(4\pi/\log p\). They occur at arbitrarily large positive and negative real heights for each \(p\). The multiplier has no boundary or center zero on the chosen strip. Its boundary and center log moduli are bounded for each fixed \(p\); the strip Green identity consequently applies without assuming canonical source/count constants. Scalar and conductor factors have harmonic logarithms and no added Green term. This proves the absolutely convergent sum in (6.6).

Differentiating \(G(u,d)\) under its integrable majorant, then setting \(v=\sinh(au)\), gives \(\partial_d\int G=\pi\). The integral is zero at \(d=0\). Thus \(\int G(u,d)du=\pi d\), and the exact period mean is \(d\log p/4\). The function of \(u\) is positive, even and decreasing on the positive half-line, so its total variation is \(2G(0,d)\). Comparing one sample and the integral in each lattice cell bounds the sum-minus-integral/spacing error by that total variation, uniformly in the lattice phase. This gives exactly (6.8), including its factor two. The weaker count estimate also has the right spacing factor.

Consequently the **added control potential** diverges uniformly while every stated fixed safe-half-plane jet error tends to zero and each prescribed finite coefficient prefix is eventually unchanged. No modulus tending to zero can estimate this potential from only those partial observations across this enlarged class. Analytic continuation itself remains unique; the result concerns stability from the named information.

The original Euler-control premises matter. The completion changes conductor from one to \(p^2\); the residue is \(D_p(1)\), and residue renormalization changes the leading Dirichlet coefficient. The numerator roots have moduli \(p^{-\beta}\) and \(p^{-(1-\beta)}\), rather than both \(p^{-1/2}\), so the altered local factor is non-tempered. The completed translated source is not the literal canonical theta source, and the added lattice forces count constants to grow with \(\log p\); shifted-source moment constants likewise are not uniform. A finite coefficient prefix is not the complete canonical coefficients or conductor constraint. These are precisely the restrictions that cannot be assigned to the controls by resemblance. This proves the scoped partial-information instability, **not** a counterexample to a theorem quantitatively using all fixed canonical data or a canonical moving-line theorem.

The inherited wider screen is also preserved: weighted-square and finite-tail families lack the complete normalized theta arithmetic/full reflection conjunction; reflected super-Gaussian and smooth/primitive families lack the unchanged theta square expansion and zeta identity. Polynomial, atomic and variable-kernel controls retain only their actual analytic/source/evolution premises. The generic Jensen inequality may hold for controls with their own admissible strip and center, and then an actual zero prevents the relevant strict small-residual threshold. No control is required to fail every coarse inequality or a box that does not contain its event.

## 6. Usable consumer inputs and next-task scope

The next task may consume the following accepted inputs, with their exact qualifications:

| Input | Accepted use | Remaining requirement |
| --- | --- | --- |
| Note28(5)–(7),(12) | Exact canonical Green/quadratic comparison and strict one-defect threshold at time zero | Independently small residual at the required centers |
| Note28(15)–(27), §6 | Compact full-source conversion, both remote tails, safe center and denominator error, valid pointwise order of limits | Evaluate the remaining compact norm with paid arithmetic/quadrature; prove uniform costs/coverage if needed |
| Note28(36) | Fixed finite Euler all-center averaged obstruction | No individual-center or arbitrary-multiplier conclusion |
| Note29(5),(24)–(26) | Uniform averaged obstruction for interval-fixed Euler products of the stated primorial length | No adaptive-center, longer-product or general-coefficient exclusion |
| Decision17(6.1)–(6.8) | Failure of stability from the stated partial safe-line jets/prefix across the enlarged Euler-control class | Quantitatively use any fixed canonical distinctions in a claimed canonical bound |

Request38's proposed default **[B] TND-O-B04 r6 — Astra/ultra**, coefficient-optimized Dirichlet-polynomial preconditioning with \(a_1=1\), \(|a_n|\le1\), \(N\le(T/2)^\theta\), fixed throughout each interval, is a legitimate **future conceptual change** outside the finite-Euler obstruction class. The primary moment theorem can be an input for that coefficient class, but the present special Euler factorization and density lower bound do not establish its gain or obstruction. The specifically proposed coefficient class already has the elementary safe-center floor \(|A_T(5/2-it)|\ge2-\zeta(5/2)\ge1/3>0\): bound its nonconstant terms by \(\sum_{n\ge2}n^{-5/2}\le\int_1^\infty x^{-5/2}dx=2/3\). Zeros elsewhere in the strip still require accounting. The combined normalization, boundary/gamma/source constants and multiplier-zero contributions must be written for any future route; the safe-center floor alone establishes neither a gain nor an obstruction. This assessment neither executes that third mechanism nor endorses its success. The Gaussian hierarchy remains available with its existing unresolved resolving-variance/transport requirements.

No failed clause or amendment of the assessed sources was found. Root identified one error in the assessor's initial future-routing wording: it had allowed a zero at the proposed safe center without using the specified bounded coefficient class. The one bounded internal correction above supplies its elementary center floor and retains possible strip zeros. This correction changes only this review and its return; it does not change Notes28–29, Decision17, the frozen request or inputs38, and it does not execute coefficient optimization. Final integrity and claim-consistency checks retained all frozen versions and the supplementary manuscript identity. The finite assessment boundary is complete: the results provide the declared comparison/acquisition machinery and precisely scoped certificate obstructions. The canonical signed estimate, all-height coverage and any RH/nonreal-zero conclusion remain unacquired.
