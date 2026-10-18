# Lower cutoff and conjugate-pair extraction after the cross-model review

17 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Recorded model: **gpt-6.1-sol (Codex)**, reasoning effort
**ultra**, verified from the session metadata. Three same-model subagents
checked the reduced-cutoff obligations, extraction and review follow-ups.
These are internal development checks, not a further cross-model or
specialist review.

**Status: proved in-note from named imports, with same-model checks only.**
The new derivation below gives

\[
 \boxed{K_t(X)\le\frac9{10}\log(X+2)+6,
 \qquad 0<t\le\tfrac12,\quad X\ge100000.}             \tag{1}
\]

Here \(K_t(X)\) counts **all complex zeros, with multiplicity**, in
\((X,X+1]\). The original Notes [01](../01_CONSUMER_AUDIT_AND_CONSTANT_LEDGER_20261017.md)
and [02](../02_EXPLICIT_OFF_AXIS_COMPARISON_AND_HIGH_HEIGHT_COUNT_20261017.md)
and the manuscript are unchanged by this round. Note 01 already contains
a link-only repair from commit `452eee4`; its reviewed bytes are recovered
by reversing that single link replacement, as checked in the execution
record. Note 02 and the manuscript retain their reviewed bytes. See
[Review 02](../../reviews/02_CROSS_MODEL_REVIEW_NOTES_01_02_AND_MANUSCRIPT_CLAUDE_20261017.md).
That review accepts the earlier results as "proved from named imports";
it does **not** cover (1).

## 1. Decision, question and scope

The reviewer recommends freezing constant optimization until an application
states its tolerance. The user's subsequent instruction explicitly requests
continued work in `notes/round-2`. This bounded continuation asks whether
one can reduce the convenience cutoff twentyfold and remove two avoidable
losses in extraction, using the same off-axis band and the same classical
inputs. It stops at (1); there is no parameter survey or search for an
optimal cutoff. No application has supplied a new kernel, domain or error
tolerance, so no computational saving or consumer gain is asserted.

This is quantitative counting infrastructure, not an RH-equivalent
criterion; see the [result-summary index](../../../../../result-summaries/README.md),
[summary 11](../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md),
the [avoid index](../../../../../avoid/README.md), and specifically
[avoid 01](../../../../../avoid/01_restating_the_target.md),
[08](../../../../../avoid/08_normalization_and_constant_slips.md),
[10](../../../../../avoid/10_numerics_ahead_of_the_question.md) and
[20](../../../../../avoid/20_volume_without_a_gain.md).
The uncovered range is now \(200\le X<100000\). Cumulative counts,
exact integer counts, conductor dependence and collision exclusion remain
outside the result. This is a restriction of coverage, not an obstruction
theorem for those tasks; see [avoid 07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md).

## 2. Inputs and normalization retained

Use Note 02's definitions

\[
 T=x/2,\quad T'=T+\pi t/8,\quad Q=x/(4\pi),\quad L=\log Q,
 \quad a=\sqrt{T'/(2\pi)},\quad N=\lfloor a\rfloor,
\]
\[
 s_+=(1+y-ix)/2,\quad s_-=(1-y+ix)/2,\quad
 B_t(z)=M_t((1-iz)/2),\quad F_t=H_t/B_t.
\]

The physical normalization is \(H_0(z)=\xi((1+iz)/2)/8\),
\(\partial_tH_t=-\partial_z^2H_t\), and
\(M_t=e^{t\alpha^2/4}M_0\), where
\(\alpha(s)=1/(2s)+1/(s-1)+\tfrac12\operatorname{Log}(s/(2\pi))\).
All logarithms of positive reals are natural. Continue to use
\(0<t\le1/2\), \(3\le y\le4\), and \(-3/2\le\Re s_\pm\le5/2\).

The source is [Polymath, arXiv:1904.12438v2](https://arxiv.org/html/1904.12438v2),
particularly (39)–(44), Proposition 6.2 and (54)–(58), Lemma 5.1(v),
Theorem 3.2 and the paired Hadamard identity (105). The general-real-part
hypotheses of Propositions 6.1–6.2 and the remainder condition in (57)
were rechecked in its HTML this round. Note 02's envelope, coefficient
summation, Gaussian moments and carrier calculations are reused with the
changed side conditions checked below. The stated constants of Proposition
6.3 are still not imported outside \(0\le\sigma\le1\).

The Arias de Reyna coefficient and remainder estimates, including the
\(C_0\) bound, and Boyd's Stirling estimate are imported **through
Polymath**. Their original papers have not been checked here; this
provenance qualification follows Review 02 §2 and
[avoid 16](../../../../../avoid/16_unchecked_imports_and_novelty_claims.md).
No new estimate for those imported results is claimed.

## 3. A remainder prefactor that survives at the lower cutoff

**Lemma.** For \(T\ge50000\), \(-3/2\le\sigma\le5/2\),
\(0<t\le1/2\), and the above \(T',a,N\),

\[
 |R_{t,N}(\sigma+iT)|
 <2e^{t\pi^2/64}|M_0(iT')|.                          \tag{2}
\]

*Proof.* We have \(D=T-3\ge49997\) and
\(a^2\ge50000/(2\pi)>87500/11>89^2\). Use Note 02's shifted
integral, with \(u=\sigma+\sqrt t\,v\). Its error envelope
\(|\eta(u)|\le(u^2+1)/D\) holds for all real \(u\). The Gaussian
moment formula (9) there is unchanged. At the new endpoint,

\[
 h=1-t/D>999/1000,\quad
 (\sigma^2+1)/D\le(29/4)/49997<1/1000,\quad
 |\sigma|/D\le(5/2)/49997<1/1000,
\]
\[
 -\tfrac12\log h\le t/(2Dh)<1/1000,\qquad
 J_0\le e^{14/(T-6)}<4/3.
\]

Thus the nontrivial moment factors for \(b=\log9,-\log2\), after
removing \(e^{b\sigma}\), remain below 2, by the same
\(2/1000+(1101/1000)^2(1000/999)/2<2/3<\log2\) calculation.

Keep \(K_u=1\) for \(u\ge0\), and
\(K_u=\max(\lfloor-u\rfloor+3,\lfloor2a^2\rfloor)\) for \(u<0\).
The negative-real-part condition \(K_u+u\ge2\) is independent of
the cutoff. The low-index coefficient compression remains valid since

\[
 .036\left(.445\frac{71}{40}+
                 \frac{.247}{89}+\frac{.098}{89^2}\right)<.029,
 \qquad \sqrt\pi<71/40.
\]

The positive-real-part coefficients need only \(a>.865\).
Consequently Note 02's pointwise majorant (11), with the separate
\(E_a=a^{-1}e^{-a^2/2}\), still holds. For its fixed-height-index
remainder, \(\nu\in(a^2,a^2+1/2]\) gives
\(\nu\log(\nu/a^2)\le1/2+1/(4a^2)<1\);
real Stirling still has prefactor 3, and
\(3a^2/10>2>\log5\). Hence \(|RS_m|\le E_a\) by Note 02's (12).
The tail enlargement to \(k\ge14\) is allowed because \(2a^2>15842\).
Its Gaussian domination uses only \(1/D<1/8\),
\(|\sigma|\le5/2\), and \(t\le1/2\); the base coefficients and
recurrence do not depend on the cutoff. Thus
\(\delta_3<1/a\), while
\(\delta_4=E_aJ_0<1/a\).

The critical change is to retain the uncompressed coefficient bound:

\[
 \delta_1+\delta_2<\frac{97.374}{a-.865}.
\]

The later shortcut \(97.374/(a-.865)\le98/a\) requires
\(a\ge42385/313\), and fails at \(a=89\). We do not reuse it.
Including \(|C_0|\le1/2\), the complete remainder bracket is

\[
 \frac{|R_{t,N}|}{e^{t\pi^2/64}|M_0(iT')|}
 <\frac23+\frac{97.374}{a-.865}+\frac2a
 <\frac23+\frac{97.374}{89-.865}+\frac2{89}
 =\frac{42215698}{23532045}<\frac95<2.
\]

All terms decrease as \(a\) increases, so this proves (2) uniformly.
The inequalities preceding the rational endpoint are strict; no equality
of rational allowances is described as a strict check. ∎

## 4. Complete comparison budget from x = 100000

The bounds for \(\alpha\), \(W_n\le1\), and both carrier ratios in
Note 02 §§3,5 remain valid. Their elementary side conditions require at
most \(x\ge8500\), \(L>1\), \(6\pi/x<1\), and the displayed phase
and logarithm reserves, all satisfied for \(x\ge100000\).
In particular,

\[
 |M_t(s_-)/M_t(s_+)|<2Q^{-y/2},\qquad
 e^{t\pi^2/64}|M_0(iT')|/|M_t(s_+)|\le Q^{-(1+y)/4}.
\]

The ordinary-term error exponent is at most
\(u(x)=[3(\log x)^2/32+7/8]/x\). Both summands decrease here;
\(\log100000<12\) gives

\[
 u(x)\le\frac{23}{160000}<\frac18,\qquad
 e^{u(x)}-1\le\frac87u(x)\le\frac{23}{140000}<\frac1{6000}.
\]

Using \(4\pi<13\), the following allowances close the entire
comparison, without changing the band:

| Contribution | Uniform upper allowance |
| --- | --- |
| Dominant sum beyond its leading term | \(\zeta(2)-1<95/147\) |
| Opposite sum | \(4Q^{-1/2}<23/500\) |
| Both ordinary approximation errors | \((242/147+23/500)/6000<3/10000\) |
| Both remainders, by (2) | \(4Q^{-(1+y)/4}\le4/Q<52/x\) |

For the opposite allowance, square the positive quantities and check
\(16\cdot13/100000<(23/500)^2\). The finite cutoff power factor
\((1+t/(16Q))^{(y+1)/4}<2\) is unchanged. We obtain

\[
 \boxed{\left|F_t(x+iy)-1\right|
 <\frac{95}{147}+\frac{23}{500}+\frac3{10000}+\frac{52}{100000}
 =\frac{5094127}{7350000}<\frac{347}{500}<\frac7{10}.}   \tag{3}
\]

This proves the new comparison on the whole stated infinite domain,
from the imported analytic statements and these explicit inequalities.
The arithmetic checker supports the finite constants, not the analytic
imports or quantification between samples; no sampling is used in this
proof. The old extraction alone already extends its old count to this
cutoff. Next we improve the extraction itself.

## 5. Two losses removable in the extraction

### A disk estimate that uses the center value and derivative together

Let \(F\) be holomorphic near a closed disk of radius \(r\), with
\(|F-1|\le q\), \(0<q<1\). Put \(f(\zeta)=(F(w+r\zeta)-1)/q\).
For \(a=f(0)\), Schwarz–Pick, or Schwarz's lemma after composing
with the disk automorphism taking \(a\) to 0, gives
\(|f'(0)|\le1-|a|^2\). Constant boundary-valued maps have derivative
zero and satisfy the same inequality. Therefore, with \(s=|a|\),

\[
 \left|\frac{F'(w)}{F(w)}\right|
 \le\frac q r\frac{1-s^2}{1-qs}
 \le\frac{2q}{r(1+\sqrt{1-q^2})}.                    \tag{4}
\]

Differentiation of the middle quotient gives its maximum at
\(s=q/(1+\sqrt{1-q^2})\). This improves the independent Cauchy and
minimum-modulus bounds, which gave \(q/[r(1-q)]\).
For \(q=7/10\), \(r=1/2\), (4) is strictly less than \(5/3\).
A wholly rational verification is

\[
 \frac{7}{5}\frac{1-s^2}{1-(7/10)s}\le\frac53,
 \quad 84s^2-70s+16=84(s-5/12)^2+17/12>0.
\]

The sharp value in (4) is about 1.63347; we use \(5/3\).

### A conjugate-pair Poisson kernel

Write \(U=X+1/2\), \(v=7/2\), and \(w=U+iv\).
The strip and Hadamard identity give Note 01's absolutely convergent
positive sum

\[
 D_t(U)=-\Im\frac{H_t'}{H_t}(w)
 =\sum_\rho\frac{v-\Im\rho}
 {(U-\Re\rho)^2+(v-\Im\rho)^2}.                     \tag{5}
\]

For a zero in the unit window, put \(h=U-\Re\rho\), so
\(|h|\le1/2\). At fixed \(h\), define \(p_h(a)=a/(a^2+h^2)\).
For \(a\in[5/2,9/2]\),

\[
 p_h''(a)=\frac{2a(a^2-3h^2)}{(a^2+h^2)^3}>0.
\]

The real source makes \(H_t\) real entire. Every nonreal zero \(\beta+ib\) is accompanied by
\(\beta-ib\), with the same multiplicity and the same window
membership. Since \(|b|\le1\), convexity gives

\[
 \frac{p_h(v-b)+p_h(v+b)}2\ge p_h(v)
 \ge\frac{7/2}{(7/2)^2+1/4}=\frac7{25}.               \tag{6}
\]

Each real zero obeys the same per-multiplicity bound directly.
Consequently

\[
 K_t(X)\le\frac{25}{7}D_t(U).                        \tag{7}
\]

The earlier proof bounded each complex zero independently and obtained
\(41/9\) instead. Pairing is legal because the window cuts only real
parts; it would require revision for a count cutting the imaginary axis
asymmetrically. Both walls satisfy the distance bound, and the chosen
half-open convention is preserved. Multiple roots are included throughout.

## 6. The resulting count and a high-height corollary

The carrier bound from Note 01 is independent of the old comparison
cutoff: for \(X\ge200\),

\[
 |B_t'/B_t|(w)\le\frac{2003}{8000}\log(X+2).
\]

For \(X\ge100000\), the entire radius-1/2 disk around \(w\) lies
in (3)'s domain. Equations (4)–(7) now prove

\[
 K_t(X)\le\frac{25}{7}
 \left(\frac{2003}{8000}\log(X+2)+\frac53\right)
 =\frac{2003}{2240}\log(X+2)+\frac{125}{21}
 \le\frac9{10}\log(X+2)+6,                           \tag{8}
\]

which is (1). No claim that the separate comparison or kernel extremizers
are simultaneously realized by theta is needed.

On the original \(X\ge2000000\) domain, Note 02's smaller
\(q_0=96624791/147000000<48/73\) is still available. At
\(q=48/73\), \(\sqrt{1-q^2}=55/73\), so (4) with \(r=1/2\)
is \(3/2\). Its monotonicity in \(q\) gives the immediate corollary

\[
 K_t(X)\le\frac{2003}{2240}\log(X+2)+\frac{75}{14}
 \le\frac9{10}\log(X+2)+\frac{11}{2},
 \quad X\ge2000000.                                 \tag{9}
\]

At \(X=2000000\), the old rounded allowance is approximately 39.41;
(1) allows 19.06 and (9) allows 18.56. These are theorem allowances,
not measured zero counts. The leading mean density is
\(\log(X/(4\pi))/(4\pi)\), approximately 0.953 there, so the result
remains loose. The improvements remove the old Cauchy additive allowance
\(574/27\) and reduce the Poisson multiplier from \(41/9\) to
\(25/7\); they do not supply exact counts or lower populations.

## 7. Review clarifications, controls and stopping point

Review 02's four requested corrections are tracked as follows. The
original manuscript is retained as the reviewed source/PDF pair; its
editorial integration is pending. This addendum states the analytic
clarifications explicitly:

- The inequality printed immediately before Polymath (60) uses
  \(1/[6(T'-.66)]\le(1/3)/[4(T-3)]\), which fails by a factor tending
  to two. The corrected numerator is \(2/3\). Note 02 and this note use
  the safe envelope \((u^2+1)/D\), so their conclusions are unaffected.
- The displayed tail for (63) can omit the height-selected remainder
  when its upper index range is empty. The separate \(E_a\) retains it;
  this small omission does not defeat Polymath's conclusions.
- The extraction losses and mean-density scale are stated in §6, and
  indirect Arias de Reyna/Boyd provenance is stated in §2. The review's
  time-zero benchmark is not used as an input or reverified here.
- The old arithmetic check is renamed to describe the endpoint equality
  it actually checks. Its code hash and replay record are refreshed;
  the original review's digest table remains a historical snapshot.

The [collision controls](../../../../../result-summaries/12_collision_controls_and_screening.md)
and [avoid 02](../../../../../avoid/02_shape_only_arguments_and_the_controls.md)
retain the same role as in Note 01 §5. Euler-factor controls do not have
the exact theta expansion used in §4; weighted-square controls do not
supply that complete expansion or full reflection; reflected smooth and
positive-primitive controls do not supply theta's arithmetic coefficients.
These are scope distinctions, **not** reports that an untested control
fails (3). Generic disk/Hadamard/conjugation implications remain valid
for every control satisfying those hypotheses. A collision does not
contradict an upper multiplicity count. The earlier Gaussian counter-kernels
likewise cannot be assigned theta's expansion merely from shape properties.

The [checker](../../numerics/round-2/check_lower_cutoff_and_paired_extraction.py)
and [execution record](../../numerics/round-2/LOWER_CUTOFF_AND_PAIRED_EXTRACTION_CHECKS_20261017.json)
check finite rational constants, the exceptional failed \(98/a\)
shortcut, and two exact adversarial examples. The paired kernel floor
is attained by a real zero at horizontal distance 1/2; counting a double
zero there retains multiplicity two. For the disk estimate,
\(F(w+r\zeta)=1+(7/10)(\zeta-2/5)/(1-(2/5)\zeta)\)
satisfies the disk premise and gives \(|F'/F|(w)=49/30\), so an
injected derivative allowance of \(3/2\) fails on the new domain's
\(q=7/10\) premise. This is an exact disk-automorphism test, not a
sample of \(H_t\). A proposed kernel floor \(3/10\) also fails;
a comparison ceiling \(69/100\) fails the sufficient budget.

Stop after this proof and replay package. The next mathematical gate is
cross-model analytic review of the changed cutoff and paired extraction.
A consumer must specify its domain, kernel, baseline and tolerance before
any application budget or further optimization. The principal-value
velocity tail requires symmetric cancellation and two-sided cumulative
information; (1) alone does not supply it. No new noncollision result,
RH implication or Newman bound is asserted.
