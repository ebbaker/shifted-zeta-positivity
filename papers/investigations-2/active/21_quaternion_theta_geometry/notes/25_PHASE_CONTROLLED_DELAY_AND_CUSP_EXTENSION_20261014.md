# Phase controlled Gaussian delay and a finite cusp extension

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded parent model **gpt-6.1-sol**, reasoning effort **ultra**, verified
from the current turn metadata. Parallel analytic and computational work,
with separate internal review, continues
[Note 24](24_PROPORTIONAL_DELAY_PHASE_OBSTRUCTION_AND_CONTINUATION_20261014.md).

**Results.** A prescribed delay depending on height repairs the outer
cross-time retained-sign failure of a purely proportional delay. The proof
controls the full zeta phase as well as the gamma phase, uniformly at
moving positive times. Separately, new complete-source interval
calculations extend the finite norm and stationary-sign cover beyond 104.
The unknown unbounded small-time region remains open.

## 1. The prescribed delay and comparison

Keep the centering fixed:

\[
 a=\pi/16,\quad b=1/4,\quad\mu=a^2+b^2,
 \qquad C_k=-h_{k+2}-2ah_{k+1}-\mu h_k,
 \quad h_k=\partial_x^kH.
\]

Use the rule proposed in Note 24 before its evaluation:

\[
 \ell(x)=\log(1+x^2),\quad B=1+t\ell,
 \quad\delta(t,x)=\frac{t}{2B},\quad\tau=t-\delta.
 \tag{1}
\]

For \(t\ge0\), \(0\le\delta\le t/2\) and \(t/2\le\tau\le t\).
Define the complete-source comparison

\[
 G_j=C_j(\tau,x),\quad P_j=h_j(t,x)G_j,
 \quad Q_j=h_j(t,x)\{C_j(t,x)-G_j/2\},\quad j=0,1.           \tag{2}
\]

On the **current** stationary set \(h_{j+1}(t,x)=0\),

\[
 \mathcal L_j=h_{j+1}^2-h_jh_{j+2}
             =\mu h_j^2+P_j/2+Q_j.                        \tag{3}
\]

Earlier stationarity is not assumed. The source multiplier is the complex
\(e^{-\delta z^2}\), not the distinct real horizontal mask
\(e^{-\delta u^2}\).

## 2. A uniform outer comparison including the arithmetic phase

**Theorem.** There is a finite unevaluated \(X\) such that, uniformly on

\[
 |x|\ge X,\quad0<t\le1/2,\quad
 \theta=t\log\frac{|x|}{4\pi}\ge\frac{13}{4},              \tag{4}
\]

both \(P_j\) and \(Q_j\) are strictly positive whenever
\(h_{j+1}(t,x)=0\), for each \(j=0,1\). With the nonzero analytic
carrier amplitudes \(A_t,A_\tau\) below and
\(\omega=\frac14\log(|x|/(4\pi))\), the lower bounds may be chosen as

\[
 P_j\ge\frac18A_tA_\tau\omega^{2j+2},\qquad
 Q_j\ge\frac12A_t^2\omega^{2j+2}.                         \tag{5}
\]

This establishes the prescribed filter's comparison on part of the
already favorable outer region. It does not lower the existing
threshold-three theorem for the full Laguerre forms or evaluate a cutoff.

**Proof.** First take \(x>4\pi\), put \(L=\log(x/(4\pi))\), and
write \(d=\delta L\). Since \(\ell>2L\),

\[
 0<d<\frac{\theta}{2+4\theta}<\frac14,
 \qquad\tau L>f(\theta):=\theta-\frac{\theta}{2+4\theta}.
 \tag{6}
\]

The function \(f\) is increasing, and
\(f(13/4)=91/30=3+1/30\). Thus
[Note 19](19_OSCILLATORY_BLOCKS_AND_PAIRED_LAGUERRE_FORMS_20261014.md)
applies uniformly at **both** times \(v=t,\tau\), with fixed positive
margin \(1/30\). Its hypotheses permit these times to decrease with
height; no lower time bound independent of height is introduced.

Use \(s=(1+ix)/2\) and the analytic functions of
[Note 17](17_UNIFORM_OUTER_CUSP_SIGNS_AND_THRESHOLD_FOUR_20261014.md):

\[
 \alpha=\frac1{2s}+\frac1{s-1}+\frac12\operatorname{Log}\frac{s}{2\pi},
 \quad w_v=s+v\alpha/2,
 \quad\mathfrak Q_v=M_0(s)e^{v\alpha^2/4}\zeta(w_v),
 \quad A_v=2|\mathfrak Q_v|>0.
\]

The four physical derivatives at each fixed comparison time satisfy

\[
 h_k(v,x)=A_v\omega^k
       \{\cos(\phi_v+k\pi/2)+O(L^{-1})\},\quad k=0,1,2,3,
 \quad\phi_v=\arg\mathfrak Q_v.                            \tag{7}
\]

The errors are uniform throughout (4). These are physical derivatives at
fixed \(v\), rather than derivatives of a selected time or an arithmetic
cutoff.

The exact relative phase is obtained from the entire carrier ratio:

\[
 D:=\phi_t-\phi_\tau
 =\Im\left\{\frac\delta4\alpha^2+
       \int_\tau^t\frac\alpha2
           \frac{\zeta'}{\zeta}(w_v)\,dv\right\}.          \tag{8}
\]

The logarithm of zeta here is its analytic prime-power logarithm in
\(\Re w>1\). Since \(\tau L>91/30\), the entire line segment
\(w_v\), \(\tau\le v\le t\), lies in \(\Re w_v\ge5/4\) for all
sufficiently large \(x\), uniformly. On this half-plane,

\[
 \left|\frac{\zeta'}{\zeta}(w)\right|
 \le\sum_{n\ge2}\Lambda(n)n^{-5/4}
 \le\sum_{n\ge2}(\log n)n^{-5/4}<18.                     \tag{9}
\]

For the final bound, the \(n=2,3\) terms are each less than 1;
\((\log u)u^{-5/4}\) decreases for \(u\ge3\), so the rest is bounded
by its integral over \([3,\infty)\), itself less than
\(\int_1^\infty(\log u)u^{-5/4}du=16\).

Using \(\alpha=L/2+i\pi/4+O(x^{-1})\) and (6), the gamma contribution
to (8) is at most \(\pi/64+o(1)\). The arithmetic contribution is at
most \(18/16+o(1)\), since \(\delta|\alpha|/2\le1/16+O(L^{-2})\).
Therefore, uniformly,

\[
 |D|\le\frac\pi{64}+\frac{18}{16}+o(1)<\frac54,
 \qquad\cos D\ge1-\frac{D^2}{2}\ge\frac7{32}              \tag{10}
\]

after increasing \(X\). Paying only the first term of (8) would omit the
arithmetic phase in the moving-time region.

At a current stationary point set \(\psi=\phi_t+j\pi/2\). Equation (7)
gives \(\sin\psi=O(1/L)\). The fixed \(2a\) and \(\mu\) terms of the
delayed residual have orders lower by at least one power of \(\omega\),
so

\[
 \frac{P_j}{A_tA_\tau\omega^{2j+2}}
 =\cos\psi\cos(\psi-D)+O(1/L)=\cos D+O(1/L).              \tag{11}
\]

The bound \(1/8\) follows from (10) by increasing \(X\) once more.
No regularity of the stationary branch is needed.

For absorption, the same current four jets give

\[
 \frac{h_jC_j(t,x)}{A_t^2\omega^{2j+2}}=1+O(1/L).          \tag{12}
\]

The exact delayed/current carrier amplitude ratio is

\[
 r:=\frac{A_\tau}{A_t}
 =e^{-\delta\Re(\alpha^2)/4}
           \left|\frac{\zeta(w_\tau)}{\zeta(w_t)}\right|.
\]

The absolutely convergent Dirichlet series for zeta and its reciprocal
bound the last factor by \(\zeta(5/4)^2\le25\). Also
\(\Re(\alpha^2)/4=L^2/16-\pi^2/64+O(L/x)\).
Because \(\ell/L\to2\), (4) gives \(d\ge1/5\) uniformly once \(x\)
is sufficiently large; for example \(\ell/L\le21/10\) suffices by
monotonicity of \(\theta/[2(1+(\ell/L)\theta)]\). Thus

\[
 r\le25e^{-L/80+O(1/L)}=O(e^{-L/80}),
\]

\[
 \frac{Q_j}{A_t^2\omega^{2j+2}}
  =1+O(1/L)-\frac r2\{\cos D+O(1/L)\}\ge\frac12           \tag{13}
\]

eventually. This proves (5) for positive heights. For \(x=-y<0\),
\(\delta(t,-y)=\delta(t,y)\) and
\(h_k(t,-y)=(-1)^kh_k(t,y)\). The delayed drift term changes sign
under reflection, while remaining within the same \(O(1/L)\) payment;
the leading products and margins are unchanged. \(\square\)

The same proof applies for every fixed \(\varepsilon>0\) on
\(\theta\ge\theta_*+\varepsilon\), with an unevaluated
\(\varepsilon\)-dependent height, where

\[
 \theta_*=(11+\sqrt{217})/8,
 \qquad 4\theta_*^2-11\theta_*-6=0.
\]

This is the threshold inherited from requiring the earlier time to satisfy
Note 19, not an optimality theorem for the filter. There is no assertion
at \(\varepsilon=0\).

## 3. Complete source and moving parameter payments

At each fixed observation point the exact complete-source identities
and complex polarization of Note 24 apply with
\(k^P_\alpha=(u^2-b^2)e^{-\delta z_\alpha^2}\) and
\(k^Q_\alpha=(u^2-b^2)(1-e^{-\delta z_\alpha^2}/2)\).
Both source coordinates and indices remain independent; both Hermitian
and bilinear terms are retained with the second multiplier conjugated in
the Hermitian part. The complete lower vertical segment still has zero
real contribution: the Gaussian and residual polynomial are real there.
The entire contour identity precedes any raw-index truncation.

Since \(0\le\delta\le1/4\),
\(|e^{-\delta(u+ia)^2}|\le M=e^{a^2/4}\). For retained set \(A\) and
its omitted set, write \(M_{A,k}\) and \(T_k\) for the complete absolute
jet masses defined in Note 24. The corresponding residual masses satisfy

\[
 B_A^P\le M(M_{A,j+2}+b^2M_{A,j}),\qquad
 B_A^Q\le(1+M/2)(M_{A,j+2}+b^2M_{A,j}),                   \tag{14}
\]

and the identical formulas hold for omitted masses with \(M_A\) replaced
by \(T\). All omitted product sectors are paid by

\[
 e^{-2ax}\{M_{A,j}B_{A^c}+T_jB_A+T_jB_{A^c}\}.           \tag{15}
\]

Imported full-index and integration-tail bounds apply on their declared
rectangles and under their stated hypotheses. Quadrature and parameter
transport errors are additional, rather than hidden in (15).

The delay is not constant under differentiation. With
\(\ell'=2x/(1+x^2)\), \(\ell''=2(1-x^2)/(1+x^2)^2\),

\[
 \delta_t=\frac1{2B^2},\quad
 \delta_x=-\frac{t^2\ell'}{2B^2},\quad
 \delta_{xx}=-\frac{t^2\ell''}{2B^2}
                  +\frac{t^3(\ell')^2}{B^3}.              \tag{16}
\]

Writing \(C_k^-=C_k(\tau(t,x),x)\),

\[
 G_{j,t}=-(1-\delta_t)C_{j+2}^-,\qquad
 G_{j,x}=C_{j+1}^-+\delta_xC_{j+2}^-,
\]

\[
 (\partial_t+\partial_x^2)G_j
  =(\delta_t+\delta_{xx})C_{j+2}^-
       +2\delta_xC_{j+3}^-+\delta_x^2C_{j+4}^-.             \tag{17}
\]

The complete-source moment majorant controls all polynomial moments, so
these differentiations are legitimate on every compact parameter domain.
The highest physical jet in (17) is \(h_{j+6}\), supplied by that source
bound; a four-jet asymptotic is not silently differentiated to obtain it.
All centering parameters remain fixed.

On a regular current stationary branch \(x=\xi(t)\),
\(\xi'=h_{j+3}/h_{j+2}\). Its exact delayed derivative is

\[
 \dot G_j=\xi'C_{j+1}^-
              -(1-\delta_t-\xi'\delta_x)C_{j+2}^-.         \tag{18}
\]

Together with \(\dot h_j=-h_{j+2}\), this gives
\(\dot P_j=-h_{j+2}G_j+h_j\dot G_j\) and

\[
 \dot Q_j=-h_{j+2}(C_j-G_j/2)
   +h_j[-C_{j+2}+\xi'C_{j+1}-\dot G_j/2].                \tag{19}
\]

A form without a jet denominator uses
\(T_j=h_{j+2}\partial_t+h_{j+3}\partial_x\): on current stationarity,

\[
 T_jh_j=-h_{j+2}^2,\qquad
 T_jG_j=-[h_{j+2}(1-\delta_t)-h_{j+3}\delta_x]C_{j+2}^-
                      +h_{j+3}C_{j+1}^-.                 \tag{20}
\]

At a singular point this tangent operator may vanish. Neither (18) nor
(20) establishes continuation or positivity through branch creation.
The pointwise outer theorem avoids that issue; the finite certificates
below cover all stationary implications directly on closed cells.

## 4. New complete-source cusp calculations

**Finite theorem.** For \(0\le t\le1/2\), \(104\le x\le112\),

\[
 |F(t,x)|=\sqrt{h_0^2+h_1^2}>10^{-17}.
\]

Both stationary implications \(h_{j+1}=0\Rightarrow\mathcal L_j>0\)
hold there. Moreover, at every such current stationary point and for
**every earlier time** \(0\le s\le t\), with the fixed centering above,

\[
 h_j(t,x)C_j(s,x)>0,\qquad
 h_j(t,x)\{C_j(t,x)-C_j(s,x)/2\}>0.                       \tag{21}
\]

Thus (21) includes both the half-time rule and the smooth rule (1) on
this finite domain, with prescribed \(\lambda=1/2\), \(K_j=0\).
The norm and full stationary signs reflect to negative heights by
physical parity; the numerical delayed products in (21) are stated for
the positive-height protocol actually tested.

The [new generator](../numerics/certify_fixed_cusp_band_extension.py) runs
the unchanged complete-source driver on two adjacent closed rectangles,
[104–108](../numerics/FIXED_CUSP_BAND_104_108_20261014.json) and
[108–112](../numerics/FIXED_CUSP_BAND_108_112_20261014.json).
Each has 32 cells: four unit spatial intervals and eight closed slabs
\([k/16,(k+1)/16]\), \(k=0,\ldots,7\). The calculation uses
python-flint 0.9.0 at 192 bits, \(a=\pi/16\), \(N=8\), \(U=3/2\),
space order 12, and time order 8. All retained quadrature, complete-index,
integration, rounding, spatial, and temporal errors are included.
Center physical jets run through order 28 and full moment payments
through order 29.

The pointwise stationary-sign test uses the driver's frozen saddle
centering; the delayed products are independently reconstructed from its
physical jets with the prescribed \(b=1/4\). The driver supplies each
whole-cell implication by either excluding stationarity or enclosing
\(\Lambda h_j^2+h_jC_j\) strictly above zero under current stationarity.
The exact audit also proves a whole-cell physical norm floor and the
normalized bound \(e^{\pi x/4}(h_0^2+h_1^2)>3000\) on the new bands.
Its rational exponential bound uses \(\pi<22/7\), avoiding reliance on
printed decimal floors.

The 128 stationary observations cover every current stationary point:

| Band | \(j=0\) observations | \(j=1\) observations |
| --- | --- | --- |
| \([104,108]\) | 24 excluded, 8 strict signs in \(107<x<108\) | 32 excluded |
| \([108,112]\) | 32 excluded | 24 excluded, 8 strict signs in \(109<x<110\) |

Paid spatial endpoint signs are opposite in each candidate cell, while
\(h_{j+2}\) has one strict sign throughout it. There is therefore exactly
one genuine current stationary point in the indicated interval at every
time. The closed-cell exclusions account for all other points and
potential branch creation; the next-derivative signs exclude creation in
the candidate cells themselves. The shared boundaries at 104 and 108
leave no gap in the cover. Combined with the previous certificates,
this extends the physical norm and stationary-sign cover to
\(0\le t\le1/2\), \(|x|\le112\), with the safe common norm floor
\(10^{-17}\).

The previous uniform residual cone \(C_0^2+C_1^2<E/9\) is not needed
for all these implications. Its unchanged enclosure test is
`INCOMPLETE` on 24 cells in the first band and 16 in the second, all
outside the candidate stationary cells. The raw records retain those
statuses and failed-cell lists. Separate norm and stationary-sign fields
pass; no failed cone enclosure is promoted into a successful cone or a
negative Laguerre form.

### Full earlier-time comparison with common spatial coordinates

The [exact auditor](../numerics/audit_fixed_cusp_band_extension.py) first
checks the half-time comparison using the affine time map from Note 24.
All 16 genuine branch/slab cases pass. It then checks (21), whose protocol
was declared before its evaluation, keeping the same centering,
absorption fraction, and zero losses.

For a current slab \(k\), the union of paid earlier slabs
\(p=0,\ldots,k\) covers \(0\le s\le t\). It conservatively includes
some \(s>t\) within slab \(k\). All observations share the current
spatial point and the same positive constant normalization
\(e^{\pi x_c/8}\). Write the two Taylor polynomials as

\[
 T_k(\eta,d)=\sum_{m=0}^{11}\sum_{r=0}^{7}c_{k,r,m}d^r\eta^m,
 \quad T_p(\eta,e)=\sum_{m=0}^{11}\sum_{r=0}^{7}c_{p,r,m}e^r\eta^m.
\]

The variables \(d,e\) independently range over \([-1/32,1/32]\),
whereas the spatial displacement \(\eta\in[-1/2,1/2]\) is shared.
To enclose absorption, the auditor forms

\[
 \sum_{m=0}^{11}\left[
 c_{k,0,m}-\tfrac12c_{p,0,m}
 +\sum_{r=1}^{7}\left(c_{k,r,m}d^r-\tfrac12c_{p,r,m}e^r\right)
 \right]\eta^m,                                         \tag{22}
\]

ranging the independent times inside each coefficient before ranging the
common \(\eta\). It then adds the complete current residual payment plus
one half the complete earlier payment, intersects with
\(-h_{j+2}-\mu h_j-C_j(s,x)/2\) only on **current** stationarity, and
takes the union over all earlier slabs. Earlier stationarity is never
used. The retained product uses the complete earlier-field hull, with its
full payments, times the current physical jet.

Ranging the two full spatial integrals separately initially left eight
absorption cases undecided. The shared-coordinate evaluation (22)
certifies all 16 while preserving the original coarse verdicts. This is
an improvement in enclosure arithmetic; the source, comparison domain,
centering, fraction, and loss remain fixed.

Conservative lower bounds, in the constant branch normalization, for
**all** earlier times are:

| Current branch | \(Z_j\widehat C_j(s,x)\) | \(Z_j(\widehat C_j(t,x)-\widehat C_j(s,x)/2)\) |
| --- | ---: | ---: |
| \(h_1=0\), \(107<x<108\), \(x_c=107.5\) | \(>15511\) | \(>7559\) |
| \(h_2=0\), \(109<x<110\), \(x_c=109.5\) | \(>6910\) | \(>3371\) |

Here \(Z_j=e^{\pi x_c/8}h_j\), and hats use that same positive scale.
Because (22) directly encloses complete fields at earlier times, it does
not apply the restricted \(\delta\le1/4\) multiplier budget (14) to a
larger delay. A general causal delay up to \(t\le1/2\) would instead
have the absolute multiplier bound \(e^{a^2/2}\), if that route were used.

The first band was declared before evaluation. After it succeeded, the
adjacent second band was declared with identical parameters before its
own evaluation; this was not a jointly blinded selection of bands.
The generator records this sequence, the actual run configuration, and
the unchanged historical driver's hard-coded model label separately.
The shared time-slab development/holdout labels do not change the fact
that every prescribed case is reported.

## 5. Validation and reproduction

The [symbolic checker](../numerics/check_phase_controlled_delay_identities.py)
and [21-check receipt](../numerics/PHASE_CONTROLLED_DELAY_IDENTITY_CHECKS_20261014.json)
verify the full delay derivatives, both mixed derivative orders, composed
heat defect, branch product rules, and exact rational phase, amplitude,
and positivity budgets. These finite checks do not replace the analytic
proof or evaluate its height.

The [new exact audit](../numerics/FIXED_CUSP_BAND_EXTENSION_AUDIT_20261014.json)
contains 1,321 passing checks, all 128 stationary observations, and all
16 genuine-branch comparisons, including their universal earlier-time
bounds and the preserved coarse verdicts. The auditor binds both the
reported sources and the files actually providing its imported transport
and exponential helpers.

Two fresh independent 192-bit runs of the complete quadrature generator
reproduce every field of both saved records after omitting only
`elapsed_seconds`. The independent exact audit reproduces its entire
saved JSON, including every rational enclosure. The
[continuation validation receipt](../numerics/PHASE_CONTROLLED_CUSP_CONTINUATION_CHECKS_20261014.json)
records stored and canonical replay hashes and the source bindings. The
[internal review](../reviews/19_PHASE_CONTROLLED_DELAY_AND_CUSP_EXTENSION_REVIEW_20261014.md)
and [review receipt](../reviews/PHASE_CONTROLLED_CUSP_INDEPENDENT_REVIEW_20261014.json)
record the separate analytic, source-payment, and numerical assessments.
This is internal LLM review, not external peer review or formal
verification of the source lemmas or interval integration library.

From this investigation's `numerics/` directory, with python-flint 0.9.0
available for the two quadrature commands:

```sh
python3 check_phase_controlled_delay_identities.py \
  --output /tmp/inv21-phase-controlled-identities.json
python3 certify_fixed_cusp_band_extension.py --x-left 104 \
  --output /tmp/inv21-cusp-104-108.json
python3 certify_fixed_cusp_band_extension.py --x-left 108 \
  --output /tmp/inv21-cusp-108-112.json
python3 audit_fixed_cusp_band_extension.py \
  --record /tmp/inv21-cusp-104-108.json \
  --record /tmp/inv21-cusp-108-112.json \
  --output /tmp/inv21-cusp-extension-audit.json
```

The symbolic checker and exact auditor otherwise need only Python's
standard library. Fresh quadrature records can have different elapsed
times, so their stored hashes need not match; compare the canonical
content with only that declared field excluded. Reproduction is claimed
for the recorded environment, without a cross-version bitwise-portability
claim. All new files stay below 1 MiB. No manuscript revision, snapshot
folder, commit, or tag is part of this research continuation.

## 6. Remaining domain and next goal

The smooth delay gives a proved outer comparison with its arithmetic
phase retained, and the bounded extension supplies additional signed
comparisons inside the unresolved small-time region. They do not cover
all heights: the outer height is unevaluated, while the possible collision
region remains unbounded as positive time tends to zero.

Any remaining positive-time collision has \(|x|>112\). The known
outer theorem still excludes unbounded collision sequences with
\(\limsup t\log(|x|/(4\pi))>3\); it has no evaluated bridge from 112.
The new delay theorem (4) is a comparison result within that already
proved outer region, rather than a replacement for it.

The next analytic goal is the signed comparison only where it is still
needed: a padded moving domain below the established outer boundary,
with a finite transition strip accounted for separately. The finite
causal theorem suggests preserving the shared spatial coordinate and
the signs of the **combined** current-minus-half-earlier source, instead
of independently paying its two amplitudes. Its global counterpart must
retain the full index and integration correlations and supply a loss
locally bounded through every candidate collision, without defining that
loss by an unknown physical energy denominator. A bound based only on
fixed-time gamma phase, the source's symmetry, or another finite norm
floor does not meet that obligation.

A concrete next deliverable is a signed estimate for arithmetic blocks
of the existing two-coordinate kernel in the inner cusp. Combine the
current and earlier coefficients before estimating, while retaining two
independent source coordinates and arithmetic indices. Pay all omitted
pairs and moving-parameter derivatives, then establish a signed bound on
a declared unbounded subdomain or a theta-specific obstruction there.
Extending another bounded strip remains useful, but does not settle this
unbounded comparison.

The conversation keeps its existing formal replay identity: number **10**,
thread `01a13d07-4714-7f83-a8f5-700a61bc5e0e`, and the same registered
archive filename. The current continuation turn is
`01a13d13-f5dc-7b50-bc6b-8e350956d176`. The preceding final reply was
confirmed captured at the beginning of this turn. The explicit refresh
and bounded exact-turn final capture remain in use; trusted native-hook
activation has not been verified.
