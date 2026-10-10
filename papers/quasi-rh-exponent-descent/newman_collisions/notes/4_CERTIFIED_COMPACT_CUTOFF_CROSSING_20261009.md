# A certified compact heat rectangle across a natural cutoff crossing

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred. Internal
same-model investigation, not independent specialist validation.

**The first compact rectangle in this branch is now certified, including a
natural integer-cutoff crossing.** With the normalizer of
[Note 3](3_NORMALIZED_HEAT_COLLISION_CRITERION_20261008.md),

\[
\boxed{\quad
\frac15\le t\le\frac3{10},\qquad
\frac{4519}{10}\le x\le\frac{905}{2}
\quad\Longrightarrow\quad Q_t(x)>\frac14>0.\quad}       \tag{1}
\]

The computation actually gives a lower bound greater than \(0.25978\).
Since \(A_t(x)>0\), this excludes every real zero of \(H_t\) on the
rectangle and hence every real multiple zero there. Evenness gives the
reflected rectangle in negative \(x\). This is a small local certificate,
not a bound for the Newman constant or evidence of uniform control toward
\(t=0\). The comparative review should update its statement that no compact
rectangle has been certified; its strategic ranking need not change.

## 1. Source theorem and coverage

The analytic input is [Polymath, Theorem 1.3, equations (6)–(24)](https://arxiv.org/html/1904.12438#S1.Thmtheorem3),
together with the analytic rewriting, symmetric normalizer, reflection,
and fixed-cutoff disk bound proved in Note 3. The source theorem was checked
again in the published arXiv text on 9 October 2026. Its domain is
\(0<t\le1/2\), \(x\ge200\), \(0\le\operatorname{Im}z\le1\);
none of these limits is extrapolated. The source proof of that theorem is
an imported input, rather than independently reproduced here.

Use

\[
X=452.2,\quad R=0.35,\quad a=0.3,\quad
\varepsilon=0.2,\quad\tau=0.3,\quad N=6.               \tag{2}
\]

The outer disks have \(\operatorname{Re}z\ge451.85>200\),
\(|\operatorname{Im}z|\le0.35<1\), and the certified inner rectangle is
\(|x-X|\le a\). The explicit Note 3 disk error, including reflection
and every cutoff correction, is enclosed as

\[
2.2474461807547521514590440333995
 <\eta_6<
2.2474461807547521514590440333996<2.248.                \tag{3}
\]

The displayed short endpoints are rounded **outward** from the full record.
Throughout the whole outer disk and all its times,
\(|Q_t-F_{t,6}|\le\eta_6\). The available derivative error on the inner
rectangle is \(\eta_6/(R-a)=20\eta_6<44.96\); it is too large to be
useful in this cell. The value alternative of the derivative interface is
sufficient for (1), so no lower bound for \(|F'|\) is invoked.

The natural cutoff is

\[
 n(t,x)=\left\lfloor\sqrt{x/(4\pi)+t/16}\right\rfloor.
\]

It changes from five to six across the exact curve

\[
x_6(t)=4\pi(36-t/16),\qquad0.2\le t\le0.3,            \tag{4}
\]

whose full range is enclosed in
\([452.1537226679109918457,452.2322624842507366767]\).
Both ends of this interval lie strictly inside \([451.9,452.5]\).
At \(x=451.9\) the natural cutoff is five for **every** certified time;
at \(x=452.5\) it is six for every certified time. The cutoff range on
the whole outer disk is also exactly \(\{5,6\}\).

We keep the single holomorphic approximant \(F_{t,6}\) on both sides.
Where the source uses five, its difference from our approximant is exactly
the sixth summand and its reflection. These terms are paid by the
\(2P_6\) correction in Note 3's equation (14). Thus the certificate neither
differentiates the jumping natural-cutoff formula nor assumes that its two
branches have the same error.

## 2. Real finite formula used in the certifier

To avoid complex interval logarithms, specialize the already proved analytic
formula to real \(x>0\). Set

\[
\begin{aligned}
d&=1+x^2,& L&=\tfrac12\log d-\log(4\pi),& v&=\arctan(1/x),\\
\alpha_r&=L/2-1/d,&
\alpha_i&=-\pi/4+v/2+3x/d,\\
\theta&=-7\pi/8-v/4+\tfrac x4(1-L)
                   +\tfrac t2\alpha_r\alpha_i,\\
a_n&=\exp\left(\tfrac t4\log^2n
              -(\tfrac12+\tfrac t2\alpha_r)\log n\right),&
\phi_n&=\theta+\tfrac12(x-t\alpha_i)\log n.
\end{aligned}                                                     \tag{5}
\]

Then exactly

\[
F_{t,N}(x)=2\sum_{n=1}^Na_n\cos\phi_n.               \tag{6}
\]

Indeed for \(s=(1-ix)/2\), \(\log|s/(2\pi)|=L\) and
\(\arg s=-\pi/2+v\); \(\arg s+\arg(s-1)=-\pi\).
Substituting those branches into Note 3's \(m_t\), \(\alpha\),
and \(p_{t,n}\) gives (5)–(6). This tracks the source logarithm branch;
there is no independent phase convention.

The implementation also evaluates the derivative formula. Its real components
are

\[
\alpha'_r=6(x^2-1)/d^2+1/d,\qquad
\alpha'_i=4x/d^2+x/d.
\]

If \(\lambda_n=(\alpha-\log n)(1+t\alpha'/2)\), and
\(b=\tfrac12\operatorname{Im}[\alpha(1+t\alpha'/2)]\), then

\[
F'_{t,N}=\sum_{n\le N}a_n
  (\operatorname{Re}\lambda_n\sin\phi_n
   +\operatorname{Im}\lambda_n\cos\phi_n)-bF_{t,N}.       \tag{7}
\]

This reproduces Note 3's analytic derivative; numerical differentiation is
not used. Its evaluation is included for reuse by later cells, while (1)
uses only (6).

## 3. Outward arithmetic and the finite cover

Run the standard-library-only
[checker](../../numerics/check_fixed_heat_checkpoint.py):

```sh
python3 papers/quasi-rh-exponent-descent/numerics/check_fixed_heat_checkpoint.py
```

The heat portion uses a 50-digit Decimal interval backend. Input decimals are
exact rationals. Addition, multiplication, division, and endpoint selection
use \(\mathrm{ROUND\_FLOOR}\) for lower bounds and
\(\mathrm{ROUND\_CEILING}\) for upper bounds. Decimal \(\exp\),
\(\log\), and square root are correctly rounded; each endpoint is widened
to its representable predecessor or successor before use. Square-root
enclosures are additionally verified by directed squaring of both bounds.
The documented
Decimal guarantees are software inputs; see the
[Python Decimal documentation](https://docs.python.org/3/library/decimal.html).
The code does not use the potentially only almost-correctly-rounded general
Decimal power operation.

For \(\pi\), it encloses the Machin identity
\(\pi=16\arctan(1/5)-4\arctan(1/239)\). Each arctangent uses 80
Taylor terms and an explicit alternating-series remainder. The small
\(\arctan(1/x)\) in (5) uses the same rigorous series with 20 terms.
Each phase interval is reduced by an integer multiple of the enclosed
\(2\pi\); any chosen integer is valid, and the reduced interval's modulus
is verified to be below four. Sine and cosine use 55 Taylor terms with the
uniform Taylor remainders
\(|z|^{111}/111!\) and \(|z|^{110}/110!\), respectively. No binary
floating-point input, sampled trig value, or numerical quadrature enters
the certificate.

The inner rectangle is covered by 12 closed spatial cells of width \(0.05\)
and ten closed time cells of width \(0.01\). On **each full parameter cell**,
interval evaluation encloses the formula (6). The smallest lower endpoint
among these 120 cells is greater than

\[
2.5072305531620089937633874951180>2.507.               \tag{8}
\]

Combining (3) and (8) proves uniformly
\(Q_t(x)>2.507-2.248=0.259>1/4\), which gives (1).
The checker compares the full 50-digit interval endpoints, rather than
relying on these rounded display constants. It also verifies the exact
cutoff-curve containment in (4). A cell-center grid cannot provide this
coverage; the interval range on each complete cell is essential.

The saved [record](../../numerics/fixed_heat_checkpoint_record_20261009.json)
contains the parameters, backend, enclosing \(\pi\) interval, full
\(\eta_6\) enclosure, minimum cell lower bound, resulting \(Q_t\) bound,
and cutoff-curve enclosure. All artifacts are small and regenerable. The
same script separately checks fixed-scale bookkeeping; those rational mesh
checks are not part of the heat theorem.

## 4. Consequence for the comparative assessment

One explicit completion condition from the comparative review has been met:
a compact rectangle, including a natural-cutoff crossing, is rigorously
excluded under the stated analytic and software inputs. This is meaningful
implementation progress over a floating reconnaissance grid or a final-
constant ledger. It is also deliberately modest. This rectangle was chosen
where the normalized value is comfortably positive; it does not cover a
zero-bearing interval, prove simplicity near an actual zero, certify the
whole finite interval from Note 3, or improve the Newman constant.

The branch's strategic role therefore remains a bounded certification or
Newman-bound side project. The next useful computational checkpoint is a
rectangle containing a genuine simple zero where the **derivative** alternative
succeeds, preferably while again paying a cutoff crossing. That likely needs
sharper analytic errors or a correction term: here the paid jump and Cauchy
radius give a weak derivative bound. A subsequent finite cover should be
reported by its explicit positive time floor and covered height range.

None of this supplies the new mechanism required as that floor tends to zero.
The established eventual cutoff \(e^{64/\varepsilon}\) still grows without
bound, and one finite union of compact rectangles cannot cover every positive
time. The result corrects the review's factual checkpoint while leaving its
main quasi-RH research priorities intact.
