# S04-T2: a signed Gaussian core estimate and the complete averaged value

19 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual model **gpt-6.1-sol (Codex)**, reasoning
effort **ultra**. Parallel same-model derivation and separate internal
review; no independent specialist review.

Status: **proved in-note**, using the established Riemann–Siegel source
contract as an imported analytic input. S04-T2 is **Complete for the
specified averaged functional**. The unsmoothed signed intermediate core,
pointwise noncollision and S04-T3's uniform residual transfer remain open.

## Frozen question, current payment and novelty boundary

This continuation follows the [task contract][task], [result summaries][summaries]
and [patterns to avoid][avoid], especially [control premises][a02],
[scoped exclusions][a07] and [preserving cancellation][a12]. It selects one
linear functional of the signed scalar in [S04 Note 01][n01] before doing
bounded numerical work. It does not assume a nonvanishing target in new
coordinates; see [the target-reformulation screen][a01].

The [earlier manuscript][earlier] already proves uniform shrinking-time
source errors, terminal-edge cancellation, raw derivative estimates,
scoped exponent-pair deficits, packet/phase obstructions and a complete
first-derivative mean-square estimate on its exponential hard window.
Those are prior work. [Heat-flow Note 22][heat22]'s stationary reflected carrier is
also prior work. The calculation here uses phase matching and Gaussian
smoothing to isolate the first mode on a different window. It is not a
new pointwise number-theoretic cancellation theorem or an improvement of
the old hard-window derivative average in the same norm.

Freeze
\[
 1\le\kappa\le2,\quad0<t\le1/20,\quad L=\kappa/t\ge20,\quad
 x=4\pi e^L,\quad N=\lfloor\sqrt{e^L+t/16}\rfloor,
\]
\[
 a_*={\kappa(4-\kappa)\over16},\quad
 b_*={\kappa(\kappa+4)\over16},\quad
 d_*={\kappa(\kappa+12)\over16},\quad
 K=N-\lfloor N^{3/4}\rfloor.
\]
The decomposition is **low 1..16, intermediate 17..K, terminal K+1..N**.
All integer endpoints and t stay fixed while the real coordinate moves.
No derivative of a floor is taken. Put
\[
 h=8,\qquad Y=8\sqrt L,\qquad
 \mu(y)={e^{-y^2/64}\over8\sqrt\pi}.
\]
For u>0 use the actual normalizer and phase from the
[current source contract][outer],
\(Q(t,u)=H(t,u)/\mathcal A_t(u)\), \(\theta(t,u)=\vartheta_t(u)\).
Define the moving leading-data scalar, with fixed integer M, by
\[
 \ell_n=\log n,\quad L(u)=\log(u/(4\pi)),\quad
 W_n(u)=\exp\{t\ell_n^2/4-(1/2+tL(u)/4)\ell_n\},
\]
\[
 T(u)=(u+t\pi/4)/2,\qquad
 \widetilde F_{t,M}(u)=2\sum_{n\le M}W_n(u)
                         \cos(\theta(t,u)+T(u)\ell_n).             \tag{1}
\]
This retains the full Gaussian amplitude drift, the heat-dependent
arithmetic phase and the common physical theta phase. Define
\[
 \mathcal M_{\rm mid}=
 \int_{-Y}^Y\mu(y)e^{-i\theta(t,x+y)}
 [\widetilde F_{t,K}(x+y)-\widetilde F_{t,16}(x+y)]\,dy,           \tag{2}
\]
\[
 \mathcal B=
 \int_{-Y}^Y\mu(y)e^{-i\theta(t,x+y)}Q(t,x+y)\,dy.               \tag{3}
\]
The primary complete observable is (3), based on Q itself, not Q/2.
The positive n=1 channel has coefficient one. Its real part is an actual
signed integral against \(\cos\theta\).

The inherited mass payment \(\sum_{n\le N}W_n(x)\le5e^{a_*/t}\)
induces the same-functional triangle payment
\(10.000001e^{a_*/t}\) for (2), including window movement. At the opening
point its envelope exceeds 425. The signed calculation below replaces
this payment by **1.5e-6** and closes the complete budget about its known
leading coefficient with radius **0.11**. This comparison is with that
named triangle payment, not with every possible signed method.

## Result

**Proposition.** Uniformly in the whole declared parameter sector,
\[
 |\mathcal M_{\rm mid}|<1.5\times10^{-6},\qquad
 |\mathcal B-1|<0.11,\qquad \Re\mathcal B>0.89.                 \tag{4}
\]
Consequently
\[
 \int_{-Y}^Y\mu(y)\bigl(Q(t,x+y)/2\bigr)^2\,dy>0.198.          \tag{5}
\]
These are averaged estimates. They neither assert \(Q(t,x)\ne0\) nor
exclude an isolated common zero of Q,Qx.

## Signed frozen transform

Exact demodulation of (1) yields two channels,
\[
 e^{-i\theta(u)}2W_n(u)\cos(\theta(u)+T(u)\ell_n)
 =W_n(u)e^{iT(u)\ell_n}
  +W_n(u)e^{-i(2\theta(u)+T(u)\ell_n)}.                       \tag{6}
\]
Freeze W at x and linearize theta only in the reflected channel.
The positive phase T is already linear, including its heat shift.
Writing \(\Omega=-\theta_x\), the full Gaussian transforms are
\[
 W_n(x)e^{iT(x)\ell_n}e^{-4\ell_n^2},\qquad
 W_n(x)e^{-i(2\theta(t,x)+T(x)\ell_n)}e^{-16\nu_n^2},
 \quad \nu_n=2\Omega(t,x)-\ell_n/2.                            \tag{7}
\]
Only the **frozen explicit finite sum** is extended to the whole line.
The physical Q integral (3) always has the finite limits shown.

For n<=N, the floor gives
\(\ell_n\le L/2+t/(32e^L)\), so
\[
 W_n(x)\le1.000001\,n^{-5/8}.                                 \tag{8}
\]
Indeed \(t\ell_n^2/4\le(\kappa/8)\ell_n+
[t^2/(128e^L)]\ell_n\); the exponent beyond the stated power is
at most \(t^2L/(128e^L)\), using \(\ell_n<L\).
The envelope reserve is maximal at t=1/20,L=20 and is below 1.000001.
The decreasing function \(f(v)=v^{-5/8}e^{-4\log^2v}\) gives
\[
 \sum_{n\ge17}f(n)\le f(17)+\int_{17}^\infty f(v)\,dv
 =f(17)+{e^{9/1024}\sqrt\pi\over4}
       \operatorname{erfc}(2\log17-3/32)
 <3.386404\times10^{-15}.                                    \tag{9}
\]
With (8), the positive intermediate channel costs <3.387e-15.
The finite sum n=2..16 is <0.099124335522 before the reserve; (8) and (9)
together give **all nonleading positive channels <0.099125**.
No arithmetic phase is replaced when computing (7); this envelope is
applied after integrating each signed mode.

For completeness the reflected gap survives the slight cutoff excess.
From Note 01's exact identities, U>=0, V>=1/x and
\(-\alpha_i\ge\pi/4-3.5/x\), whence
\[
 2\Omega\ge L/2+{t\pi\over8x}-{1+1.75t\over x^2}.
\]
Subtracting \(\ell_n/2\le L/4+t/(64e^L)\) leaves
\[
 \nu_n\ge L/4+{t\pi\over16x}-{1.0875\over x^2}\ge L/4.        \tag{10}
\]
The last step uses \(tx\ge4\pi e^L/L\), increasing for L>=20.
A deliberately weaker gap L/4-1e-9 also suffices. Thus the entire
reflected frozen family costs
\[
 5e^{3L/16}e^{-16(L/4-10^{-9})^2}<4.1\times10^{-172}.           \tag{11}
\]
Its logarithmic derivative is \(3/16-8(L/4-10^{-9})<0\).
This suppresses the reflected channel under (3); it does not delete the
reflected channel pointwise.

## Pay movement and truncation on the whole window

Here x>=4*pi*exp(20)>6.09e9 and Y/x<5.869e-9. At fixed t,n,
\[
 |(\log W_n)'(u)|={t\ell_n\over4u},\qquad
 |W_n(x+y)/W_n(x)-1|\le .250003|y|/x.                        \tag{12}
\]
The second inequality follows from t*ell_n<1.000001, u>=x-Y, and the
exponential increment bound; it is uniform for |y|<=Y.
Differentiating \(\Omega=\frac12\Re[\alpha(1+t\alpha'/2)]\)
from the real-axis formulas gives
\[
 |\theta_{xx}(t,u)|=|\Omega_x(t,u)|<.250003/x.                 \tag{13}
\]
One explicit ledger is V<=1/u+3/u^3, |alpha'|<=2/u,
|alpha''|<=3/u^2 and t|alpha|<1.050001, together with
\(\Omega_x=V/4+(t/8)\Im(\alpha'^2+\alpha\alpha'')\).
The reflected phase Taylor remainder is therefore at most
.250003*y^2/x. Paying both channels in (6), first amplitudes then the
reflected phase, costs at most
\[
 \sum W_n(x){.500006|y|+.250003y^2\over x}
 \le {5e^{3L/16}\over x}(|y|+y^2).
\]
Use the exact complete Gaussian moments
\(\int\mu|y|=8/\sqrt\pi\), \(\int\mu y^2=32\) to obtain
\[
 E_{\rm move}\le {5e^{3L/16}\over4\pi e^L}
                   (8/\sqrt\pi+32)<1.274\times10^{-6}.        \tag{14}
\]
This bound is decreasing as exp(-13L/16). It applies to any subset of
the retained modes, so is charged **once** after recombining low/core/edge.
The sharper movement payment in the checker is <3.59e-7; (14) is the
chosen conservative common ledger.

The frozen two-channel polynomial's Gaussian tail costs
\[
 E_{\rm tail}\le10e^{3L/16}\operatorname{erfc}(\sqrt L)
 <1.08\times10^{-7}.                                        \tag{15}
\]
The expression decreases: Mills' inequality gives the logarithmic
slope of erfc(sqrt L) less than -1, while 3/16<1. Check its exact endpoint
L=20. Equations (9), (11), (14), (15) sum to <1.382e-6, proving (2)'s
claim. The terminal family is included by the same transform and common
payments; no known pointwise edge estimate is counted as a new result.

## Complete real-axis source payment across cutoff crossings

The window is much wider than Note 01's radius-1/L disk. Also
\(tL(x-Y)\) can be slightly below one. Consequently that disk theorem
and its kappa-domain bound cannot simply be reused at x+y.
Instead apply the published [Polymath Theorem 1.3, (23)–(24)][polymath]
at each real point, using common **real-axis** positive majorants from
[the local source contract][outer]. Put
\[
 x_\pm=x\pm Y,\quad q_\pm=x_\pm/(4\pi),\quad
 \alpha_-={1\over2}\log q_--4/x_-^2,
\]
\[
 V_n=\exp\{-\ell_n/2+t(\ell_n^2/4-\alpha_-\ell_n/2)\},\quad
 r_n=\max_{\pm}|\log(q_\pm/n^2)|,
\quad U_n=\exp{t^2r_n^2/16+.626\over x_--6.66}-1.
\]
For an actual natural integer m in this window the common remainder is
\[
 \eta_N\le\max_m\left\{2\sum_{n\le m}V_nU_n+E_m^C+
          2\sum_{\min(m,N)<n\le\max(m,N)}V_n\right\},          \tag{16}
\]
\[
 E_m^C=q_-^{-1/4}\exp\left\{-{t\log^2q_-\over16}
 +{2.48\over m-.125}
 +{3\sqrt{\log^2q_++\pi^2/4}+10.44\over x_--12}\right\}.
\]
This is the published real-axis estimate with vertical radius zero:
the two normalized gamma channels have modulus one, so K=1. No
radius-Y holomorphic estimate or Cauchy derivative is inferred.

Here are explicit uniform reductions, not a scan. Let
\(\xi=Y/x\), \(\rho=-\log(1-\xi)\) and
\(\Delta=\rho/2+4/x_-^2\). Each decreases from its L=20 endpoint.
The whole continuous cutoff width obeys
\[
 \sqrt{q_++t/16}-\sqrt{q_-+t/16}
 \le {Y\over4\pi\sqrt{q_-}}<.00013.                         \tag{17}
\]
Thus its endpoint floors differ by at most one, and N is one endpoint.
Every point needs at most **one** fixed-N correction. Such an index j
has \(|\log j-L/2|<.0001\): compare j with e^(L/2) plus or minus
one and the t/(32e^L) continuous-cutoff reserve.
For \(\delta=\log j-L/2\), direct algebra gives
\[
 \log V_j+b_*/t=-\delta/2+t\delta^2/4
                   -{t\over2}(\alpha_--L/2)(L/2+\delta).
\]
Its absolute value is <.000051, so V_j<1.001e^(-b*/t) and the jump
cost is <2.002e^(-b*/t).

For AB the mass proof of Note 01, extended through the possible extra
index, gives \(\sum V_n<5.1e^{a_*/t}\). Explicitly its coefficient is
at most \((5+1.001e^{-L/2})e^{.500001\Delta}\).
Since \(t r_n\le2+t\rho\), the numerator defining U_n is
<.87600001, and U_n<.9/x_-. Hence
\[
 E^{AB}< {9.18e^{a_*/t}\over x_-}
          <e^{-d_*/t}<.001e^{-b_*/t}.                        \tag{18}
\]
The identities used are a*-kappa=-d* and (d*-b*)/t=L/2>=10.
For C, its leading log differs from -b*/t by at most rho/2;
m>22000 and
\((3(L+\rho+\pi/2)+10.44 )/(x_--12)<1.3e-8\).
Thus \(E_m^C<1.001e^{-b_*/t}\). Combining gives
\[
 \sup_{|y|\le Y}|Q(t,x+y)-F_{t,N}(x+y)|
 <3.1e^{-b_*/t}\le3.1e^{-6.25}<.005984408.                   \tag{19}
\]
The outward checker gives a coefficient below 3.000246 before choosing
3.1. These bounds apply directly to the entire real window even when
its translated kappa lies just outside [1,2].

Finally transfer the exact finite scalar to (1) on this same window.
The real-axis identities hold for all u>=x_-:
\[
 \alpha_r-L(u)/2\in[-u^{-2},0],\qquad
 0\le\alpha_i+\pi/4\le3.5/u.
\]
Thus each positive mode is multiplied by
\(e^{\delta_n}\),
\(\delta_n=-t\ell_n[\alpha_r-L(u)/2+i(\alpha_i+\pi/4)]/2\),
with \(|e^{\delta_n}-1|<1.754/x_-\).
Using \(\sum W_n(u)\le e^{.250001Y/x_-}5e^{a_*/t}\) gives
\[
 E_{\rm model}:=\sup_{|y|\le Y}|F_{t,N}-\widetilde F_{t,N}|(x+y)
 <{17.6e^{a_*/t}\over x_-}<1.23\times10^{-7}.                \tag{20}
\]
This repeats the elementary per-mode proof with window constants rather
than silently importing the old endpoint-domain proposition.

## Complete ledger, diagnostics and interpretation

All payments below refer to the **same** complete functional (3).
The source and model payments are integrated with total Gaussian mass
less than one; movement and tails are charged once for all modes.

| Payment | Uniform upper bound |
| --- | ---: |
| Positive n>=2 leakage, including all intermediate and terminal indices | 0.099125 |
| All frozen reflected modes | 4.1e-172 |
| Model movement, both channels | 1.274e-6 |
| Frozen-polynomial Gaussian tail | 1.08e-7 |
| Exact finite scalar to leading-data scalar on window | 1.23e-7 |
| Complete real-source remainder, including one possible cutoff jump | 0.005984408 |
| Total | <0.106; reported radius 0.11 |

The outward unrounded ledger is <0.105110347. This proves (4).
Since \(m=\int_{-Y}^Y\mu=\operatorname{erf}(\sqrt L)<1\), Cauchy–Schwarz
and the reality of Q give
\[
 |\mathcal B|^2\le m\int_{-Y}^Y\mu Q^2,\qquad
 \int_{-Y}^Y\mu(Q/2)^2>{.89^2\over4}=.198025>.198.
\]
This proves (5). It is a weighted **value** energy, not the old hard-window
**derivative** mean square. The support length is 16*sqrt(L), whereas
the Gaussian width is fixed. Converting to the normalized unweighted
mean on that support yields only
\(\frac1{2Y}\int_{-Y}^Y(Q/2)^2>.099\sqrt\pi/\sqrt L\).
This exposes the changed norm rather than claiming a same-norm improvement.

The [checker and reproduction guide][numerics], [192-bit record][r192]
and [256-bit replay][r256] check outward constants after analytic monotone
reductions. They also evaluate the **complete finite frozen Gaussian
transforms**, retaining actual phases and heat shifts, at exactly three
prescribed points: (kappa,t)=(1,1/20),(1,1/21),(21/20,1/20).
Their cutoffs are 22026,36315,36315, with the same declared split.
These diagnose the transform and signed recombination; they are not
physical-source quadrature, a parameter cover or the proof of uniformity.
Source identities are checked before execution. The [separate review][review]
includes a fresh 192-bit replay and missing/stale-input checks.

The [collision-control catalog][controls] was screened by premise.
Prime/local-factor and finite-prime profiles lack the full reflected,
unchanged theta expansion; super-Gaussian and positive-primitive controls
lack that source expansion; Euler deformations change coefficients and
level; polynomial and counter-kernel controls lack the theta source;
positive-channel controls lack the complete signed physical observation.
Those constructions cannot inherit constants (19)–(20). Moreover an
averaged energy bound may hold at a source's isolated collision.
There is **no new average-to-pointwise acceptance interface**. The
[fresh inherited control replay][control-record] rejects five source-event
boxes and the Euler negative-sign witness using their own errors in the
unchanged consumer. It does not assert that (5) rejects those events.

**Decision and handoff.** The named signed-core payment and its effect on
the full averaged budget meet S04-T2's bounded estimate gate. Stop this
functional here. No second derivative is consumed, so S04-T1 stays
Conditional. S04-T3 stays Waiting: neither (4) nor (5) supplies the
pointwise residual increment and anchor control needed there. Next work
must select that missing pointwise arithmetic input, or explicitly design
an additional argument converting averaged information into a useful
physical constraint. A nonzero smoothed coefficient alone does not do so.

[n01]: 01_PHASE_RETAINING_FULL_CUTOFF_SCALING_20261018.md
[task]: ../../research-overview/01_RESEARCH_OVERVIEW_GOALS_AND_TASKS_20261018.md
[outer]: ../../../manuscript/positive_arithmetic_packets/sections/10_outer_exclusion.tex
[earlier]: ../../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/newman_collision_reductions.tex
[polymath]: https://arxiv.org/html/1904.12438v2#S1.Thm3
[summaries]: ../../../../../../result-summaries/README.md
[avoid]: ../../../../../../avoid/README.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[numerics]: ../numerics/README.md
[r192]: ../numerics/S04_GAUSSIAN_CORE_192_20261019.json
[r256]: ../numerics/S04_GAUSSIAN_CORE_256_20261019.json
[control-record]: ../numerics/S04_T2_CONTROLS_20261019.json
[review]: ../reviews/02_GAUSSIAN_SIGNED_CORE_INTERNAL_REVIEW_20261019.md

[heat22]: ../../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/notes/22_SIGNED_PAIR_TRANSFORMS_AND_STATIONARY_REFLECTION_20261010.md
