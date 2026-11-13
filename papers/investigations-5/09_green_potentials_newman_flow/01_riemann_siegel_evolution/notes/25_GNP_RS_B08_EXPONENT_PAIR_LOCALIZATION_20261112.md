# GNP-RS-B08 — exponent-pair improvement below the quarter-power scale

12 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Chat0006, thread
`01a1d151-91b1-7663-8f10-07d0b4f94163`. Actual backend model and reasoning
effort are unavailable in the recorded source configurations. Three
analytical helpers contributed source, shifted-sum and ledger checks;
their inherited settings are not independently identified.

**Status: proved in-note from named classical and inherited inputs, with
contributing separate-agent internal checking.** [Review13][review]
records that scope. The bounded B08 request from [Note24][return07] is
completed with a localization gain from 1/4 to **17/72**, a decrease of
1/72 in the exponent. B07's exact boundary repair is retained. The same
logarithmic residual, Green mean and fixed-threshold density rates hold
on the shorter intervals. No every-center estimate is proved.

This is a quantitative averaged milestone under [target01][a01]. Read
[result summaries][results], especially [heat-flow cluster11][r11], and
[avoid][avoid], especially [premise02][a02], [scope07][a07],
[separate-bounds12][a12] and [unchecked-imports16][a16]. Section 7 applies
[controls12][controls] to the premises actually used. The classical
exponent-pair estimate is credited; no new exponent pair or literature
priority is claimed.

## 1. Statement and unchanged field

Retain the complete theta field, carrier, physical equation, strip and
Green geometry of [B06][b06] and [B07][b07]. In particular c=1,
\(L_X=\log(X/(4\pi))\), and physical time \(1/L_X\) is fixed
throughout each spatial window. The prime cutoff P is fixed throughout
the outer interval. Write
\[
 \mathscr R(U,\ell;P)=\ell^{-1}\int_U^{U+\ell}R_P(X,1)dX,
 \qquad
 \mu_P=\sum_{\substack{k>1\\(k,D_P)=1}}k^{-3/2}\le2P^{-1/2},
 \quad D_P=\prod_{p\le P}p.
\]
All definitions of the exact residual and Green value are those of B06
Section 1 and B07 Section 1, without a source or clock substitution.

**Theorem.** For each fixed \(0<\rho\le19/72\), all sufficiently
large real U, every integer \(2\le P\le\lfloor L_U^2\rfloor\), and
\(U^{17/72+\rho}\le\ell\le U\),
\[
 \boxed{\left|\mathscr R(U,\ell;P)-\mu_P\right|
 \le C\left(\frac{\sqrt{\mu_P}}{L_U}+L_U^{-2}\right)
       +O_\rho\left(U^{-\min(1/144,\,9\rho/28)}\right).}      \tag{B08.1}
\]
At \(P_U=\lfloor L_U^2\rfloor\), this gives
\[
 \mathscr R(U,\ell;P_U)=\mu_{P_U}+O_\rho(L_U^{-3/2})
                      =O_\rho(L_U^{-1}),                    \tag{B08.2}
\]
\[
 \ell^{-1}\int_U^{U+\ell}J_{1/L_X}(X)dX=O_\rho(L_U^{-1/3}),
 \quad
 \ell^{-1}|\{X\in[U,U+\ell]:J_{1/L_X}(X)\ge h\}|
                    =O_{h,\rho}(L_U^{-1})\quad(h>0).        \tag{B08.3}
\]
The new power remainder is a convenient sufficient bound, not optimized.
Finite constants and onsets depend on the named fixed field provider,
fixed smoothing function and fixed exponent-pair theorem. Their numerical
values are not evaluated or certified. B06/B07 remain valid as stated.

The auxiliary arithmetic arm is unchanged:
\[
 A(u)=\sum_{n\le N_u}w_n(u)e^{i\nu(u)\log n},\quad
 N_u=\lfloor\sqrt{u/(4\pi)}\rfloor,\quad
 w_n(u)=n^{-3/4}\exp((\log n)^2/(4L_u))\le n^{-5/8},
\]
\[
 \nu(u)=u/2+\pi/(8L_u),\quad
 \phi(u)=u(L_u-1)/2+\pi/8+7\pi/4,\quad
 S=A+e^{i\phi}\overline A.
\]
B07 (B07.4) retains the complete-field error \(O(u^{-1/4})\), including
the fractional-cutoff correction and residual. Its HDA fixed-chart,
buffer and physical-time hypotheses retain their inherited internal-review
status. This note does not re-audit that provider.

## 2. The exact shifted sum and the applicable classical estimate

Retain B07's exact Fubini weight W and subprobability measure
\(d\sigma=2W(x)dx/\ell\), as well as its fixed nonnegative smooth
majorant \(\chi((u-U)/\ell)\). On \(r_*\le\ell\le\sqrt U\),
where \(r_*=(32/\pi)\log(2U)\), B07 Sections 2–4 pay all boundary,
freezing and cutoff effects and reduce the tail norm to the exact frozen
pair expansion. Comparable pairs are \(n=m+h\), \(m\in[N,2N)\),
\(1\le h<m\), with all head/full-cutoff restrictions retained in an
interval \(I_{N,h}\). Their contribution is
\[
 \sum_h\sum_{m\in I_{N,h}}a_h(m)e(f_h(m)),\qquad e(t)=e^{2\pi it},
\]
\[
 f_h(x)=t\log(1+h/x),\quad t=\nu_U/(2\pi)\asymp U,
 \quad\nu_U=U/2+\pi/(8L_U),
\]
\[
 a_h(x)=w_x(U)w_{x+h}(U)
      \widehat\chi\bigl((\ell/2)\log(1+h/x)\bigr).          \tag{B08.4}
\]
The unchanged amplitude bound is, for each fixed A,
\[
 \sup|a_h|+\operatorname{TV}(a_h)
       \le C_A N^{-5/4}(1+\ell h/N)^{-A}.                  \tag{B08.5}
\]
It holds on every permitted interval with its endpoints included. B07
proves it using coefficient derivatives and an additional power of Fourier
decay. No independence of prime phases is used.

The formal classical input is [Robert, Sections 5.1–5.2, equation (20)][robert].
For a fixed exponent pair \((k,l)\) and fixed real \(\alpha<1\), there
are fixed \(Q,\epsilon,C\) such that the following holds. Let
\(g_\alpha(x)=x^\alpha/\alpha\) when \(\alpha\ne0\). If
\(F=(T/N^\alpha)g_\alpha+v\) on an interval inside \([N,2N]\), with
\[
 |v^{(q)}(x)|<\epsilon(T/N^\alpha)|g_\alpha^{(q)}(x)|,
                   \quad1\le q\le Q,
\]
then
\[
 \left|\sum_{m\in I}e(F(m))\right|
       \le C\{(T/N)^kN^l+N/T\}.                           \tag{B08.6}
\]
The theorem includes arbitrary subintervals. Its printed A/B transforms give
\[
 (0,1)\xrightarrow{B}(1/2,1/2)
 \xrightarrow{A}(1/6,2/3)
 \xrightarrow{A}(1/14,11/14)
 \xrightarrow{B}(2/7,4/7).                                \tag{B08.7}
\]
The [source record][sources] identifies the exact author copy and passage.
Section 5.1 has an inconsistent positive-alpha parameter list; its opening
definition and Section 5.2 explicitly quantify over real \(\alpha<1\).
We use that stated convention. The same pair applied to a shifted logarithmic
ratio is independently corroborated in [Bourgain–Watt, Lemma 13.3,
equation (13.37)][bw]. Our application to the nonsymmetric ratio below is
checked directly; no change of the integer summation grid is made.

## 3. Uniform phase-class verification, including the extra term

Conjugate the phase and set
\[
 F_h(x)=-t\log(1+h/x)=-t\int_0^h(x+s)^{-1}ds,
 \quad F_0(x)=-th/x,
 \quad \alpha=-1,\quad T=th/N.
\]
Since \(g_{-1}(x)=-1/x\), we have
\((T/N^{-1})g_{-1}(x)=F_0(x)\), exactly in the source normalization.
For every q≥1,
\[
 \frac{|(F_h-F_0)^{(q)}(x)|}{|F_0^{(q)}(x)|}
 =1-\frac1h\int_0^h(1+s/x)^{-q-1}ds
 \le\frac{(q+1)h}{2x}.                                   \tag{B08.8}
\]
The inequality follows from \(1-(1+y)^{-q-1}\le(q+1)y\), y≥0.
For the fixed Q and epsilon associated with pair \((2/7,4/7)\) and
alpha −1, choose
\[
 \delta_0=\min\{1/2,\epsilon/(Q+1)\}>0.
\]
For \(h\le\delta_0N\), the relative error in (B08.8) is at most
\(\epsilon/2\), simultaneously for every \(q\le Q\). This remains
true on every cutoff-restricted interval and all its partial intervals.
The constants are independent of U, N, h, ell, P and Y. Thus (B08.6) gives
\[
 \boxed{\sup_{\substack{I\subset I_{N,h}\\I\text{ an interval}}}
 \left|\sum_{m\in I}e(f_h(m))\right|
       \le C\{(Uh)^{2/7}+N^2/(Uh)\}}
              \qquad(1\le h\le\delta_0N).                 \tag{B08.9}
\]
Both terms are retained. This invokes the phase-class theorem, not an
unsupported inference from a few derivative magnitudes.

For the remaining comparable pairs \(h>\delta_0N\),
\(\log(1+h/m)\ge\log(1+\delta_0/2)>0\). Their Fourier factor
is at most \(C_{A,\delta_0}\ell^{-A}\). The square of the complete
absolute coefficient sum is \(O(U^{3/8})\); hence all these pairs
together cost \(O_{A,\delta_0}(U^{3/8}\ell^{-A})\). This same bound
pays noncomparable pairs. It is applied to the full population once,
without a dyadic-block logarithm. No large shift is discarded without
payment, and no condition \(h/N\to0\) is silently imposed on all pairs.

## 4. Shift summation and the complete-tail estimate

Partial summation using (B08.5) and (B08.9) bounds one dyadic block by
\[
 C N^{-5/4}\sum_{h\ge1}(1+\ell h/N)^{-A}
          \{U^{2/7}h^{2/7}+U^{-1}N^2h^{-1}\}.
\]
As in B07, extending the small-shift upper bound to all positive h only
increases this nonnegative majorant. For fixed A≥4 and q>0,
\[
 \sum_{h\ge1}h^{2/7}(1+qh)^{-A}\ll q^{-9/7},\qquad
 \sum_{h\ge1}h^{-1}(1+qh)^{-A}\ll\log(2+q^{-1}).           \tag{B08.10}
\]
For the second estimate, split at \(1/q\) when q<1; for q≥1 the sum
is bounded by \(q^{-A}\zeta(A+1)\). Thus every block is bounded by
\[
 \boxed{C\{U^{2/7}N^{1/28}\ell^{-9/7}
          +U^{-1}N^{3/4}\log(2+N/\ell)\}.}                \tag{B08.11}
\]
Both N powers are positive. The exact all-pair partition by the smaller
index m, already proved in B07, therefore permits a geometric sum up to
\(N\le N_U\ll\sqrt U\), giving
\[
 C\{U^{17/56}\ell^{-9/7}+U^{-5/8}(1+\log U)\}.            \tag{B08.12}
\]
The logarithm here pays the explicit \(N/T\) remainder. It is not an
extra loss from a blockwise Cauchy–Schwarz estimate.

Let
\[
 \mathcal E_8(U,\ell)=U^{17/56}\ell^{-9/7}
              +U^{3/8}\ell^{-4}+U^{-5/8}(1+\log U).
\]
For \(2\le Y\le N_{U-2\sqrt U}\), B07's diagonal estimate and
\(O(U^{-5/8})\) freezing cost now give
\[
 \boxed{\begin{aligned}
 \int|A-A_Y|^2d\sigma&\le A_1:=C_8(Y^{-1/4}+\mathcal E_8),\\
 \int|A|^2d\sigma,\quad\int|A_Y|^2d\sigma
                    &\le A_0:=C_8(1+\mathcal E_8).
 \end{aligned}}                                           \tag{B08.13}
\]
The fixed \(C_8\ge1\) depends on the bump and the fixed exponent-pair
constants, including delta_0. The full/head index sets obey the same pair
argument. Freezing is still paid on the full support
\([U-2\ell,U+3\ell]\): weight and small-phase drift cost
\(O(\ell U^{-13/16})\), and every floor crossing contributes to an
\(O((1+\ell/\sqrt U)U^{-5/16})\) amplitude allowance. This retains
both the cutoff jumps and the \(\pi/(8L_u)\) phase correction. There is
no differentiated floor function or differentiated exact-field remainder.

The leading term in (B08.12) becomes \(U^{-9\rho/7}\) when
\(\ell\ge U^{17/72+\rho}\). This is the promised gain over B07's
quarter-power range. It still takes absolute values across shifts after
applying a stronger, justified estimate to each inner arithmetic sum.

## 5. Retuned full residual ledger and Green transfer

Use B07's exact weighted finite-head ledger (B07.26), with A0,A1 from
(B08.13). For clarity its remaining quantities are
\[
 H=\prod_{p\le P}(1-p^{-3/4})^{-1},\quad
 T_M=M^{-\eta}F_{3/4-\eta}(P),\quad
 F_s(P)\le\exp(C_sP^{1-s}),
\]
\[
 L_0=L_{U-r_*},\quad K_0=\lfloor M\rfloor Y,\quad
 a_0=C_2/(4L_0)+C_0Y^{-1/8}+C_0M^{-1/8},\quad
 D_0=2\sqrt{\mu_P}a_0+a_0^2,
\]
\[
 s_0=150000K_0(1+\log K_0)/\ell,\quad
 b_0=(\sqrt{\mu_P}+a_0)^2+s_0,\quad
 c_0=8000H^4Y^{3/4}/(\ell L_0).
\]
Here \(C_0\le25\), \(C_2\le81(32/e)^2\) as in B06; \(T_M\)
is the multiplier tail, distinct from the local phase scale T in Section 3.
The complete ledger is
\[
\begin{split}
 |\mathscr R-\mu_P|\le{}&D_0+s_0+\tfrac12c_0
 +8H^2\sqrt{A_0A_1}+4T_M\sqrt{A_0b_0}+2T_M^2A_0+2HT_Mb_0\\
 &+C_{\rm clk}H^2(U^{-1/32}+r_*U^{-9/16})
                   +(4/\pi)\mu_PU^{-4}.                  \tag{B08.14}
\end{split}
\]
B07 proves this for the exact W, retaining all reflected rational
frequencies in the head and paying the omitted arm and multiplier tails.
In particular \(\operatorname{TV}(W)\le1+\ell/(2U^4)\),
\(1-(4/\pi)U^{-4}\le\int d\sigma\le1\); no pointwise boundary
envelope is reintroduced. The complete-field and physical-clock errors
remain paid before Fubini.

Retune the cutoffs, after establishing (B08.13), to
\[
 M=U^{1/9},\qquad Y=\lfloor U^{1/9}\rfloor,\qquad\eta=1/8.
                                                               \tag{B08.15}
\]
Keeping both at U^(1/8) would lose the new shorter range through s0.
With \(\ell\ge U^{17/72+\rho}\), the powers are instead:

| Cost before subpower product factors | Bound |
| --- | --- |
| New shifted tail norm square | \(U^{-9\rho/7}\) |
| Its residual square comparison | \(U^{-9\rho/14}\) |
| Head norm-square tail after square root, coefficient head tail, multiplier tail | \(O(U^{-1/72})\) |
| Retained same-arm off-diagonal | \(O(U^{-1/72-\rho}(1+\log U))\) |
| Retained reflected term | \(O(U^{-11/72-\rho}/L_0)\) |
| Large shifts and noncomparable pairs, norm square | \(O(U^{-41/72-4\rho})\) |
| Extra exponent-pair remainder and freezing, norm square | \(O(U^{-5/8}(1+\log U))\) |

The unchanged clock cost is smaller than the slow retained errors.
Also \(H\le e^{C_{3/4}P^{1/4}}\) and
\(T_M\le U^{-1/72}e^{C_{5/8}P^{3/8}}\). After a finite
rho-dependent logarithm-absorption gate, A0,b0 are bounded and (B08.14)
yields
\[
 |\mathscr R-\mu_P|\le C(\sqrt{\mu_P}/L_U+L_U^{-2})
 +G(P)\{U^{-1/72}+U^{-9\rho/14}\},\quad
 G(P)=C\exp\{C(P^{1/4}+P^{3/8})\}.                         \tag{B08.16}
\]
Impose the common finite gate
\[
 \log G(L_U^2)\le\tfrac12\min(1/72,9\rho/14)\log U.        \tag{B08.17}
\]
This proves (B08.1) when \(\ell\le\sqrt U\). For
\(\sqrt U\le\ell\le U\), B06 with its parameter \(\rho=1/8\)
has remainder \(O(U^{-1/128})\), which is stronger than the claimed
\(O(U^{-1/144})\) cap. This overlap retains the same cutoff and clock.

All B07 gates are retained: inherited provider/buffer/correction onsets on
\([U-r_*,U+\ell+r_*]\subset[U/2,3U]\); \(L_0\ge16\),
\(r_*\le U^{17/72+\rho}\), \(U-2\sqrt U\ge U/2\),
\(2\le Y\le N_{U-2\sqrt U}\), \(1/4\le\nu'\le1/2\),
\(T_1(P)\le L_U^2\), and the reflected derivative gates
\[
 2\log Y+3\log M\le(7/8)L_0,
\]
\[
 \frac\pi{8(U-r_*)^2}(L_0^{-2}+2L_0^{-3})
       (2\log Y+3\log M)\le1/(12U).
\]
The frequency exponent is now 5/9<7/8, so a fixed margin remains. The
fixed source constants Q,epsilon,delta_0 introduce no growing parameter.
Replacing P by L_U² in increasing product gates gives a single onset for
all allowed P. No effective numerical threshold is claimed.

Finally \(\mu_{P_U}=O(L_U^{-1})\) gives (B08.2). The unchanged E06
transfer used in B06/B07 is
\[
 J_{1/L_X}(X)\le\delta/4+R_{P_U}(X,1)/(2\delta^2)+C/L_U.
\]
Choosing \(\delta=L_U^{-1/3}\) gives the Green mean in (B08.3).
For fixed h, choose a sufficiently small constant delta and use Markov on
the residual. All reference, prime and exterior terms of that transfer
remain paid. No new Green sign inequality is assumed.

## 6. Scoped limitation and the every-center gap

At \(\ell=U^{17/72}\), the leading shifted-tail majorant is order
one. **This limits the displayed fixed-pair, absolute-shift majorant,
not the actual shifted correlation or all localized methods.** The finite
head has a positive margin there; the leading unpaid improvement is now
in the complete shifted tail, not the boundary or head parameters.

A useful bookkeeping diagnostic makes the scope more precise. If a fixed
exponent pair \((k,l)\) is used in the same way, its main term in a
weighted block is
\[
 U^kN^{l-k-1/4}\ell^{-k-1}.
\]
At the largest arithmetic scale \(N\asymp\sqrt U\), its power
threshold is
\[
 \beta(k,l)=\frac{k+l-1/4}{2k+2}.                           \tag{B08.18}
\]
Beating 1/4 in this formula requires \(k+2l<3/2\); our selected
pair meets that test. Moreover, for the conventional pair range
\(0\le k\le1/2\), \(1/2\le l\le1\),
\[
 \beta(k,l)\ge1/8.
\]
Indeed \(8(k+l-1/4)-(2k+2)=6k+8l-4\ge0\).
This is only a floor for the largest-block **power majorant produced by
this recipe**: the n^(-5/8) envelope, a per-shift exponent-pair main term,
and absolute summation over h. It is not an impossibility theorem about
exponent-sum methods, a lower bound on a tail norm, or an assertion that
1/8 is attained by a proved pair. Even retaining sharper weights alone
does not remove the largest-scale issue, where the envelope is comparable
to the actual weights. A new use of correlation or a different consumed
estimate remains outside this calculation.

The exact sum before absolute shift summation is still (B08.4). Its
useful h range is \(h\lesssim N/\ell\). A further bounded pass can
test a joint m,h estimate against (B08.11), without assuming that stronger
per-shift powers by themselves yield a pointwise theorem.

The total allowed Green mass is still \(O(\ell L_U^{-1/3})\), which
diverges on the new shortest intervals. A localized positive defect fits
inside that allowance. No every-center small value, sufficient maximal
estimate, or quantitative persistence lower bound along
\(X\mapsto(1/L_X,X)\) has been proved. Spatial smoothing does not
supply the moving-time derivative near a collision. The c=1, fixed geometry,
block-constant cutoff, bounded-height and unevaluated-onset qualifications
remain. Full-c, shrinking-depth, time-zero and positive-threshold exclusions
remain open, with parent GNP and sibling RSCT ownership unchanged.

## 7. Controls, records and continuation

The generic classical exponent-pair inequality is not claimed to distinguish
theta from every collision control. Literal reuse of the complete result
requires the canonical field/arm identification, amplitudes, common height
phases, divisor cancellation and physical readout. The [control catalog][controls]
is screened as follows, preserving B07's full named classes:

| Control | Missing premise for this canonical application |
| --- | --- |
| Euler-factor and translated sources; earlier heat counter-kernels | Unchanged complete theta source, canonical coefficients/completion and corresponding arm identity. |
| Weighted finite-square, finite-tail and finite-prime-orbit controls | Complete unchanged coefficient sequence and full reflection, beyond their retained finite arithmetic data. |
| Reflected super-Gaussian, smooth-shape and positive-primitive controls | Canonical integer-square/Dirichlet arithmetic of the complete arm. |
| Atomic, exact finite-profile and compact continuous profile controls | Full theta coefficients and profile, not only finitely many observations. |
| RH-conditional normalized endpoint controls | Ordinary Dirichlet-series arithmetic of unmodified theta. |
| Fixed-amplitude variable-kernel controls | Actual cosine oscillator/Newman operator. |
| Relaxed positive-measure profiles | An actual integer zero configuration identified with the complete physical field. |
| RSCT calibrated multiplicative models | Actual common height trajectory beyond calibrated data and the full physical Green-window law. |

The four-family comparison and reflection rigidity retain their conjunction
and domain qualifications. These are premise screens, not claims that an
isolated collision must contradict an asymptotic mean. No witness is moved
to our time band or tested numerically. Both negative statements in Section 6
are scoped to the displayed majorants; neither stops the canonical problem.

The [assessment][review], [execution record][record] and [source-use record][sources]
record the checks and their limits. Source hashes identify versions only.
[Note26][return08] gives continuation and model-change guidance; the
[sole register][progress] owns task status. No new manuscript snapshot,
source/clock change, numerical campaign or E08 is issued.

[b06]: 21_GNP_RS_B06_GROWING_CUTOFF_MEAN_20261112.md
[b07]: 23_GNP_RS_B07_LOCALIZED_TAIL_AND_EXACT_BOUNDARY_20261112.md
[return07]: 24_GNP_RS_B07_RETURN_AND_MODEL_CHANGE_20261112.md
[return08]: 26_GNP_RS_B08_RETURN_AND_MODEL_CHANGE_20261112.md
[review]: ../reviews/13_GNP_RS_B08_INTERNAL_ASSESSMENT_20261112.md
[record]: ../numerics/15_GNP_RS_B08_INPUTS_AND_CHECKS_20261112.json
[sources]: ../references/02_GNP_RS_B08_EXPONENT_PAIR_SOURCE_USE_20261112.md
[progress]: ../research-progress/01_GNP_RS_RESEARCH_PROGRESS_20261110.md
[robert]: https://perso.univ-st-etienne.fr/rool6510/robert-2015-indag.pdf
[bw]: https://arxiv.org/pdf/1505.04161v1
[results]: ../../../../../result-summaries/README.md
[r11]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a16]: ../../../../../avoid/16_unchecked_imports_and_novelty_claims.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
