# E05 assessment calculations for the E03 acquisition theorem

8 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Actual backend model and reasoning
effort are not recorded in accessible capture metadata. Three fresh,
inherited-configuration read-only assessors assisted this internal review.
The root assistant also authored E03; neither fresh helper context nor
agreement constitutes independent specialist review.

**Status: analytical verification supporting E05 r1 assessment.**
This note records calculations against the original frozen
[Note06][proof]; it does not replace that proof, change its constants,
introduce a new acquisition mechanism, or supply a favorable value.
[Review06][review] owns the assessment disposition; the [sole register][register]
owns live task status.

## 1. Local lemma, growth and tail verification

Jensen counts zeros with multiplicity. If k zeros occur in |z|<rho,
then k log(R0/rho)<=A, hence k<=n. Dividing out the finite outer-disk
Blaschke factors preserves |h|<=1 by the maximum principle. On the
zero-free inner disk, Harnack gives -log|h|<=51A on |z|<=r0.
The factors satisfy
\[
 |b_j(z)|\ge |z-a_j|/(R_0+r_0)=|z-a_j|/B.
\]
For q_*=e^{51A}t<1 and k>0, product<q_* forces at least one ratio
less than q_*^{1/k}; k line intersections have total length at most
2Bk q_*^{1/k}<=2Bn q_*^{1/n}. The cases k=0 and q_*>=1 are covered
as written. The line-sublevel statement is therefore valid; no
two-dimensional trace substitution occurs.

The logarithmic kernel identity is
\[
 \log(1+h/u)=\int_u^\infty\frac{h}{t(t+h)}dt,\qquad u,h>0.
\]
Tonelli and the sublevel bound give
\[
 C\int_0^h t^{1/n-1}dt+
 Ch\int_h^\infty t^{1/n-2}dt
 =C\frac{n^2}{n-1}h^{1/n}.
 \tag{A1}
\]
The imposed n>=2 pays the second integral. Integrating the same
sublevel bound with dt/t on (0,1) gives Cn and pays local log
integrability, including all real multiplicities.

The canonical disk has Re s>=1/4; s=0 is outside and s=1 is removable
in F. The safe anchor at Re s=5/2 is independent of the real boundary
zeros. For t_v=log(1+abs(v)), c0<3/5 implies L0>1, so
\[
 n_v\le2+A_v/\kappa\le N_0(1+t_v),\qquad A_v/n_v\le\kappa.
\]
Thus
\[
 \log M_v+C_vn_v
 \le[\log26+2Be^{51\kappa}N_0^2](1+t_v)^2.
 \tag{A2}
\]
This is the exact E2 constant, not a newly enlarged bound.

On each kth unit tail interval, K<=e^{-ak}/8. Two sides yield
1/4. With k=R+j and S=abs(X)+R+2, use
1+log(S+j)<=(1+log S)(1+j) and
\[
 \sum_{j\ge0}q^j(1+j)^2=\frac{1+q}{(1-q)^3}.
 \tag{A3}
\]
These steps reproduce Note06 (11), retaining the height factor.
The compact error is nonnegative, so multiplying each local error
by its actual maximum weight w_k is legitimate.

## 2. Literal source, gamma and prime verification

Keep the exact reflected prefix of Note06 (13). Split its error into
arithmetic omissions on [-V,V] and the **complete** source outside.
The factor e^{8abs(u)} for abs(Im z)<=8 combines with the source
majorant to give precisely e^{9abs(u)} and
delta_H=[5C2(N)Q+B0 Q^{>V}]/2. No odd-derivative matching is required.

For the radial tail let T=pi e^{4V}. Direct substitution gives
\[
 \mathcal Q^{>V}=\frac1{2\pi^{9/4}}
       \int_T^\infty t^{13/4}e^{-t}dt.
 \tag{A4}
\]
The polynomial-exponential majorant in Note06 (15) follows from
t^{13/4}<=t^4 for t>=pi and repeated elementary integration.
The arithmetic-term ratio
((n+1)/n)^4 e^{-pi(2n+1)} decreases, so the stated geometric
C2(N) bound is valid, including N=0 for the constant B0.

The reciprocal-gamma product at [DLMF 5.8.2](https://dlmf.nist.gov/5.8#E2),
freshly passage-checked, yields
\[
 |\Gamma(w)^{-1}|\le |w|
       \exp\{\gamma\Re w+\pi^2|w|^2/12\}.
\]
Putting w=s/2 gives the inherited compact multiplier with the exact
1/(2abs(s)) factor and exponent denominator 192. This multiplier
is never extended over the unbounded boundary.

For the prime baseline, direct substitution gives
\[
 \widehat K((\log n)/2)=\frac1{n^2+n^{-2}},\qquad
 \frac{n^{-9/2}}{n^2+n^{-2}}-n^{-5/2}
 =-\frac{n^{-5/2}}{1+n^{-4}}.
 \tag{A5}
\]
Absolute convergence permits the operations. The xi normalization
and abs(q)=1 on the lower boundary retain exactly one +G(X,1).
A second q correction would double count it. Integer Q>=2 gives
sum_{n>Q}n^{-5/2}<=2Q^{-3/2}/3; no tail is silently assigned to
a noninteger cutoff.

## 3. An explicit witness for the future quadrature bounds

Note06 §8 asserts existence of finite Mhat and L on the real compact
interval. The following calculation verifies that assertion without
changing the proof or executing an evaluator.

Write W=abs(X)+R, let mathcal B be Note06's multiplier, and define
\[
 \mathcal B_{\rm c}(W)=32\pi^{3/8}
 \exp\left\{\frac38+
 \frac{\pi^2[9/4+(W+1/2)^2]}{192}\right\}.
 \tag{A6}
\]
For a circle of radius 1/2 about any real x with abs(x)<=W,
\[
 1/4\le\Re s\le3/4,\qquad
 |s|^2\le[9/4+(W+1/2)^2]/4.
\]
The same gamma-product estimate gives |D0|<=mathcal B_c on this
collar: 8/abs(s)<=32, pi^{Re(s)/2}<=pi^{3/8}, and
gamma Re(s)/2<=3/8. The collar excludes s=0 and the reciprocal
gamma introduces no pole there. Cauchy's derivative bound therefore
gives sup_{real compact}|D0'|<=2mathcal B_c.

The positive finite prefix is bounded by the complete majorant.
Differentiation of its finite Fourier integral is justified directly:
\[
 \sup|\widehat H|\le\frac{B_0\mathcal Q}{2},\qquad
 \sup|\widehat H'|\le\frac{V B_0\mathcal Q}{2}
 \quad\hbox{on the real compact}.
\]
Consequently valid explicit choices are
\[
 M_{\rm hat}=\frac{\mathcal B B_0\mathcal Q}{2},\qquad
 L=\frac{(2\mathcal B_{\rm c}+V\mathcal B)B_0\mathcal Q}{2}.
 \tag{A7}
\]
These are finite for the already fixed tuple and source cutoffs.
No new arithmetic smallness premise is involved.

The regularized log is 1/delta Lipschitz as a function of its complex
field value. Thus Note06's L_g=aH/16+L/(16delta) is valid. For a cell
of width ell and midpoint c, integral|x-c|dx=ell²/4. Summing gives
a midpoint error at most R L_g Delta/2, hence the written conservative
bound R L_g Delta. Positive midpoint weights sum to at most
(2R)/16=R/8. Node field errors e_F therefore cost at most the actual
weight sum times e_F/delta, plus the explicitly reserved arithmetic
errors. Interval **width**, twice a symmetric radius, pays eta_eval.

This checks a finite-existence claim, not an affordable algorithm.
One must either evaluate the exact declared approximant and propagate
node noise, or declare a surrogate with a uniformly certified total
field error and integrate that surrogate. Note06 states both
conventions separately; they must not be mixed.

## 4. Assembly, finite choices and scope

With L_tail the exact omitted signed integral, the identity is
\[
 U-J=(\mathcal I-L_{\rm comp})
       +(\mathcal T-L_{\rm tail})+(P-P_Q+\beta_Q).
\]
The brackets lie in [0,E], [0,2T], [0,2beta]. The h/6, h/6,
h/3 allocation sums to h. The explicit Q bound and finite minimum
over positive delta thresholds meet these allowances. The common-M
variant reapplies the generic lemma with one normalization, avoiding
any assumption that local ceiling-dependent error formulas are monotone.

The review accepts these calculations as acquisition of the actual
signed value with controlled error. It acquires no favorable value.
The controls may obey the generic lemma with their own constants;
missing canonical identities prohibit silently supplying c0 or P,
rather than proving that every resulting inequality fails.

The E03 acquisition estimates require no mathematical repair. One E05
additive evidence/control-scope clarification is recorded next. It is
separate from E03's historical scope-clarification cycle.

## 5. One additive evidence and control clarification

Note06 §10 says: “The inherited obstructions retain E02's
accepted-with-additive-correction status; this assembly does not reassess
their primary mean-value theorem.” Read literally after §9's three
obstructions, that sentence overextends E02's assessment level.
The correct evidence allocation is:

* OG Note01 and Note02 retain E02's accepted-with-additive-correction status,
  with the real mixed-term correction in OG Note03 attached.
* OC Note04 retains its stated “proved in-note; proof-author self-check
  only” level. E02 did not assess it.
* E03/E05 do not newly audit the primary mean-value theorem. That
  inherited theorem belongs to the short-polynomial obstruction,
  not the OC harmonic-distance argument.

This addendum is the authoritative evidence qualification for E05's
acceptance of Note06. Original proof bytes and all mathematical claims
remain unchanged.

The ten rows of Note06 §9 cover the controls12 families. The broader
avoid02 “Instead” rule also names older counter-kernels and SUSY controls.
Complete that analytical screen here:

| Additional control or scoped obstruction | Premise comparison for E03 |
| --- | --- |
| Collision counter-kernels q and q_(T,a) | Their sources/transforms are not the literal theta/xi source. They cannot inherit its Euler anchor, prime baseline or source-error identity. Generic acquisition may apply with their own paid hypotheses; no collision time is transplanted to time zero. |
| SUSY smooth-density control | Its replacement of discrete prime measure by e^r dr changes the arithmetic object while retaining the named archimedean data. Canonical P cannot be assigned to it. No statement about its own Green potential is invented. |
| SUSY two-channel exclusion | It concerns the specified norm-factorization architecture and support lengths. E03 retains a signed log integral and is not that architecture. The exclusion is not a universal field counterexample or an upper-value estimate. |

The actual sources are routed by [cluster11][heat] and
[cluster04][positive] and the stated [control rule][screen].
Only the relevant source/class passages were checked, not the full
proofs of these older results. The [supplemental input record][supplement]
binds the additional passage sources without changing Inputs13.

These evidence and control additions form **one bounded additive
clarification cycle**. No E03 estimate, constant, source, observable,
error allocation or fixed premise changes. No B02 r2 trigger is present.
No frozen proof/input, manuscript, parent/sibling or shared-summary
file was edited.

[proof]: 06_TND_OG_E03_COMPLETE_SIGNED_LOG_ACQUISITION_20261108.md
[review]: ../reviews/06_TND_OG_E05_CLAIM_LEVEL_ASSESSMENT_20261108.md
[register]: ../research-progress/01_TND_OG_GREEN_RESOLVENT_RESEARCH_PROGRESS_20261107.md
[heat]: ../../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[positive]: ../../../../../../result-summaries/04_positive_constructions_and_scoped_obstructions.md
[screen]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[supplement]: ../research-progress/handoffs/13_TND_OG_E05_SUPPLEMENTAL_CONTROL_INPUTS_20261108.json

