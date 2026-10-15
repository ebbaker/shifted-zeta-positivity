# Review of the signed cutoff lemma and threshold eight thirds

14 October 2026 (America/New_York). Prepared for Edward Baker with substantial
LLM assistance. Recorded parent model **gpt-6-astra**, reasoning effort
**ultra**, independently checked in source metadata for parent turn
`01a13d8f-6ec4-7583-810c-ed920ba56c29`. The reviewing agent used inherited
context; its own model and effort were not independently verified from
source metadata. This is internal LLM review, not external peer review or
formal verification.

**Assessment: approved within the stated subdomain. No mathematical
correction is required.**
[Note 31](../notes/31_SIGNED_CUTOFF_LEMMA_AND_THRESHOLD_EIGHT_THIRDS_20261014.md)
establishes the outer sufficient threshold 8/3 with a fixed positive margin,
and then proves both versions of its signed cutoff conclusion on that
independently established region. It does not prove the original proposed
lemma throughout the strip beginning at theta=5/2.

## 1. Arithmetic estimates and the new domain

The primary source was independently read through the web tool:
Olivier Robert, *On van der Corput's k-th derivative test for exponential
sums*, Theorem 3, printed p.8, and Sections 5.1--5.2, printed pp.11--13:
[author PDF](https://perso.univ-st-etienne.fr/rool6510/robert-2015-indag.pdf).
The fourth-derivative specialization retains both terms and applies to a
short interval of length J by replacing J with its upper bound M. The
derivative size is uniformly comparable to T/M^4. The exponent-pair
definition permits an arbitrary segment inside [M,2M], includes the
exact logarithmic phase through g_0, and retains the secondary M/T term.
Thus the maximal shortened-block use of (6) needs no completion argument.
The stated A/B chain gives (1/9,13/18). Conjugation handles either phase
sign; fixed phase normalizations affect only constants.

The weighted exponents in (9) are correct. At theta=8/3 and delta=0,
the principal values are 0 and -2/507 on [1/4,5/13], and -2/507 and 0
on [5/13,1/2]. Convexity bounds the complete intervals. The fourth-test
secondary term is smaller by at least 1/52 on its interval; the pair's
secondary exponent is at most -3/4 before the disc perturbation.

For theta_u>=8/3+epsilon/2, the principal improvement is at least
3epsilon/128, while delta<=epsilon/100 costs at most epsilon/200.
The resulting margin 59epsilon/3200 leaves 27epsilon/3200 after the
claimed epsilon/100 decay rate. This pays the harmless extension of beta
beyond 1/2 after increasing the height. Uniformity is valid because
theta_u<=ell/2. The weight is decreasing, and Abel summation with the
maximal block estimates pays shortened terminal blocks. An interval may
cross the switch in its right endpoint: the bound uses its left endpoint
M, so this creates no omitted segment.

The low-index exponent is at least 1+epsilon/16+3s/16. The factor
(theta_0+s)2^(-3s/16) is bounded uniformly in s>=0, which handles growing
theta_u. The ordinary zeta tail has the stated decay from sigma>=7/6.
Thus the weighted replacement remains uniform on the shrinking disc,
not merely at real points or bounded values of theta.

The inherited complete error estimates remain sufficient: e_A+e_B is
O(L^2 u^(-3/4)) and e_C,0 is O(u^(-5/12)). All three imported errors
are retained. The carrier comparison, reflection, Cauchy differentiation,
and fixed-order carrier derivative estimates are the previous analytic
argument with the new half-plane bound. No floor cutoff is differentiated.
This review checks that substitution and its hypotheses; it does not
claim a new proof of the imported Polymath approximation theorem.

## 2. Physical signs and the cutoff constants

The constants in (12) are valid. The first-pair normalized norm is at least
1-4eta=1/2 when eta=1/8. Keeping the nonnegative squared error in each
Laguerre expansion gives 1-4eta-eta^2=31/64, as in Note 17. Multiplying by
4|Q|^2 and the appropriate omega power gives the displayed 31/16.
The present checker deliberately verifies the weaker 15/32 normalized
Laguerre bound; this is compatible with, but does not itself verify, the
sharper constant used in the note. The sharper constant was independently
checked from the written expansion. Since omega>=1 and
|zeta(w)|>=1/zeta(7/6), the energy bound E>=2Gamma^2/zeta(7/6)^2 follows.

The complete-source moments (13) are finite and dominate all retained
absolute moments uniformly in 0<=t<=1/2. In the full paired identity,
combining the two frequency squares gives 2(y^2+z^2); retaining its factor
1/4 then gives precisely the bound in (14). Both pair sectors and all
independent coordinates remain present.

The coefficient (15) is prescribed from the source moments and the
explicit nonzero carrier. It uses no sampled energy floor or observed
adverse quotient. Combining (12) and (14) proves (3), with the stated
factor of two spare. This coefficient is independent of N and locally
bounded, but is not bounded uniformly over the unbounded height range.
Indeed, at a=pi/16 the previous carrier estimates give growth of the form
exp(pi x/8+O((log x)^2)). Consequently this is the locally bounded
coefficient version of the target, not a theorem with one numerical A_j
for all heights. The note makes this distinction explicitly.

For (16), N>=8 ensures V_N>=1. On v>=1, log(v+a)<=v, and

\[
 \frac{d}{dv}\left[e^{-4v}(v^2/2+13v)\right]
 =e^{-4v}(-2v^2-51v+13)<0.
\]

The value at v=1 is less than beta_0/2. Thus the complete moment integrand
is bounded by C_0 exp[-(beta_0/2)e^{4v}] for k<=3. Integrating using the
increasing derivative of (beta_0/2)e^{4v} gives exactly

\[
 T_k^{(N)}\le \frac{C_0}{2\beta_0N^2}
                 e^{-(\beta_0/2)N^2}.
\]

The common-coordinate complement is the whole tail v>=V_N; there is no
additional uncounted raw-index rectangle. Applying Note 19's complete
pair-tail bound and using e^(-2cN^2)<=e^(-cN^2) proves the displayed B_j.
The full positive sign from Theorem 1 then proves (4). The tail constants
are uniform in t and positive height; the sign assertion about the
retained form still requires domain (1).

Equation (17) is exact on the full stationary set. Its two ingredients
are L_j=-h_jh_{j+2} and |h_j|<=sqrt(E) for j=0,1. It introduces no
stationarity assumption for the retained jets. This bound for J is an
error identity, not a new adverse-product estimate in the unresolved cusp.

## 3. Replay, limitations, and continuation

The [checker](../numerics/check_hybrid_cutoff_lemma.py) was independently
run with its output outside the repository:

```sh
python3 papers/investigations-2/active/21_quaternion_theta_geometry/numerics/check_hybrid_cutoff_lemma.py \
  --output /tmp/inv21-hybrid-cutoff-review-replay.json
```

It passed **84 exact rational checks**. The replay was byte-identical to
the [stored receipt](../numerics/HYBRID_CUTOFF_LEMMA_CHECKS_20261014.json),
and all four recorded source hashes matched the current files. The receipt
SHA-256 was
`b3a8bbb8a86bef1b7118b490ce171b14c16d27a7091ea21207240ed73c0e5f1b`.
The listed hashes bind the checker, Notes 19 and 30, and the manuscript;
the receipt does not hash Note 31. It verifies finite algebra, not the
external theorems, infinite integrals, or complex-disc uniformity.

The exact theta=8/3 boundary is excluded. The estimates in this proof lose
both a low-index summability margin and a high-index endpoint margin
there; epsilon cannot simply be set to zero. The portion
5/2<=theta<=8/3, the smaller cusp, and the finite transition from height
112 to the unevaluated X_epsilon remain unresolved. The result improves
asymptotic coverage and supplies the cutoff conclusions on that coverage;
it does not establish a logarithmic-loss mechanism through an unknown
collision. Its conditional statement about the limsup of hypothetical
collision sequences has the correct scope.

No broad numerical sweep, quadrature, new finite-height certificate,
manuscript revision, commit, tag, or snapshot was made in this review.
Only this review file was created. Chat capture remains the parent's
responsibility; this review does not certify its lifecycle.
