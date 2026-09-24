# First-prime continuation: local metrics, essential cancellation, and a failed energy approximation

24 September 2026. Prepared for Edward Baker with substantial LLM assistance.

**Model:** GPT-6 (Codex; developer-provided identity).  
**Reasoning effort:** not exposed; not inferred.  
**Baseline:** `6a6e2b9e40fd01f142264071c95d41cfeed9d814`, with the existing uncommitted arithmetic-storage opening package.  
**Status:** first research session. New internal analytical reductions and outward-rational certificates for specified local bounds and witnesses; separate floating finite-input diagnostics. Specialist review is outstanding. No all-input first-prime contraction, Sonin comparison, all-depth theorem, or physical realization is established.

## 1. Outcome

The [opening program](ARITHMETIC_STORAGE_PROGRAM_AND_GOALS_20260924.md) specified
the first-prime append

\[
L=11/20,\qquad h=1/5,\qquad R=L+h=3/4,\qquad w=10^{-3}.
\]

Both local windows are prime-free, but their join crosses a=log2. The first
analysis establishes three useful facts.

1. **The local prerequisites survive.** Internal all-input certificates give
   Q(0,L) >= 0.015 I and Q(0,h) >= 0.44 I, with uniform small-shift control.
   Thus the local energy metrics and both diagonal defect inverses exist at
   this benchmark. Those prerequisites are not the remaining obstruction.
2. **The prime must be kept together with the archimedean and pole terms.**
   A certified test function has negative gamma/pole energy at R=3/4, while
   the exact first-prime contribution makes its complete energy positive.
   Consequently an upper bound obtained by separately bounding the norms of
   the archimedean and prime mixed operators cannot prove the desired relative
   bound: the archimedean relative norm alone already exceeds one.
3. **The inherited 128-mode lower-energy proxy cannot close this join.**
   A rational three-cosine test on each local window violates its relative
   coupling condition. The same test has strictly positive energy for the
   complete arithmetic form. This is a rigorous obstruction to that proxy,
   not evidence of noncontractivity of the arithmetic transfer.

Finite-input calculations for the **complete** local metrics are favorable:
the relative coupling quotient reaches approximately 0.99647753 at 96 cosines
per window. These are approximate lower bounds on the unknown all-input norm,
not upper bounds or certificates. The remaining task is an all-input estimate
that retains the necessary gamma energy and the signed cancellation.

## 2. Exact mixed operator and a noncompact prime block

Use the parent's ordinary interval L2 norm and generator convention

\[
G_{s,R}=\begin{pmatrix}G_{s,L}&0\\-2H_s&G_{s,h}\end{pmatrix}.
\]

Reflect the old coordinate to r=L-y. The local symmetric forms commute with
reflection. Write

\[
H_s=H_s^A+c_p\cosh(sa)\mathcal R_a,
\qquad c_p=\frac{a}{\sqrt2},\qquad a=\log2,
\]
\[
H_s^A(t,r)=\left(\frac{e^{-5(t+r)/2}}{1-e^{-2(t+r)}}-e^{(t+r)/2}\right)
\cosh(s(t+r)),\qquad 0<t<h,\ 0<r<L,
\]
\[
(\mathcal R_a f)(t)=\mathbf1_{\{0<a-t<L\}}f(a-t).
\]

The reflected prime term is supported on t in (a-L,h), with r=a-t.
In physical old coordinates it reads f(L+t-a). It comes directly from the
generator coefficient −sqrt2 log2 cosh(s log2) at delay log2; no approximation
to a delta distribution is involved.

The active segment has length R-a, approximately 0.05685282. Nevertheless,
\(\|\mathcal R_a\|=1\). Restriction to that segment followed by reflection
is an isometry on its supported subspace. In fact, for **any finite-rank**
orthogonal projections P_L and P_h,

\[
\|(I-P_h)\mathcal R_a(I-P_L)\|=1. \tag{2.1}
\]

To see this, choose a unit function on the active old segment orthogonal to
the finitely many old head functions and to the pullbacks of the new head
functions. There are only finitely many constraints on an infinite-dimensional
space. Its image has the same norm and lies in the new complement. The reverse
inequality follows from the contraction property of all three factors.

Thus neither a short overlap nor a larger finite head makes the prime tail
small in the unweighted operator norm. An unweighted Hilbert–Schmidt tail
bound for this block is also unavailable. Energy weighting or additional
structure is essential; (2.1) does not exclude either.

At zero shift the complete central form has the block representation

\[
Q_{0,R}=\begin{pmatrix}Q_{0,L}&-H_0^*\\-H_0&Q_{0,h}\end{pmatrix}. \tag{2.2}
\]

All statements about relative norms below use this normalization and these
signs. In particular, a positive prime coefficient in H subtracts its mixed
pairing in Q; the sign of that pairing depends on the test functions.

## 3. All-input local metrics

The [preceding coupling proof](../../../critical-path/notes/CUMULATIVE_OPERATOR_COUPLING_CERTIFICATE_20260920.md)
provides the finite-tower lower operator and its cosine representation. This
session evaluates that reduction at the new lengths; it does not import the
old constants unchanged.

Let a_n=2n+1/2 and let S_(1/a_n) be the causal exponential averaging operator
with kernel a_n exp(−a_n u). With the fixed physical local coefficient w0,

\[
T_{M,\ell}=w_0I+\sum_{n=0}^{M-1}\frac2{a_n}(I-\Re S_{1/a_n})
+2|c_\ell\rangle\langle c_\ell|-2|s_\ell\rangle\langle s_\ell|,
\]

where c_ell(x)=cosh((x−ell/2)/2), s_ell(x)=sinh((x−ell/2)/2).
Every omitted gamma form is positive, so Q(0,ell) >= T_(M,ell).
For the local certificate only, round w0 downward to −5.372184.

Use M=128, N=32 orthonormal cosines in the head, and explicit metric-cross
columns up to J−1=1023. For the head/complement split, the certificate gives
an exact rational lower head A, a complement floor c, and
\(BB^*\preceq r^2 A\), including the uncomputed columns. Young's inequality
then supplies

\[
Q_{0,\ell}\succeq (1-\eta)A\oplus(c-r^2/\eta)I.
\]

| Quantity | Old length 11/20 | New length 1/5 |
|---|---:|---:|
| Head floor | 0.016 | 0.45 |
| Raw complement floor | 3.16 | 3.59 |
| Relative metric-cross squared bound r² | 0.018 | 0.001 |
| Young parameter eta | 0.04 | 0.01 |
| Complement floor after paying for cross terms | 2.71 | 3.49 |
| Retained all-input floor | **0.015** | **0.44** |

For reproducibility, the uncomputed metric columns use the inherited bound

\[
|B_{ij}|\le E_i\rho_j/k_j^2,\qquad
\sum_{j\ge J}\rho_j^2/k_j^4
\le\frac2\ell\left(\frac\ell\pi\right)^4\frac1{3(J-1)^3}.
\]

Their physical squared Gram bounds are below 3.154e−6 and 1.738e−7,
respectively. They are added to the finite Gram and rounding errors before
outward LDL sign tests. The head alone is not the certificate.

The implementation reuses only the inherited rational interval, log, exp,
square-root, and LDL utilities. It records the inherited source hash. Feature
rounding and matrix-entry errors are explicitly removed in the sign tests;
floating eigensolvers are not used in this certificate.

## 4. Uniform shift control and a precise conditional target

The old local estimate s²/8 should not simply be reused at length 0.55.
For either new local length ell, the complete bounded difference is the causal
kernel −2H_0^A(u)(cosh(su)−1). Using
\(e^{-5u/2}/(1-e^{-2u})\le1/(2u)\), Young's convolution inequality gives

\[
\|G_{s,\ell}-G_{0,\ell}\|
\le s^2\cosh(s\ell)
\left[\frac{\ell^2}{4}+\frac{e^{\ell/2}\ell^3}{3}\right]. \tag{4.1}
\]

Uniformly for 0 <= s <= w, the certified upper bounds are below
1.487e−7 and 1.295e−8. Thus both instantaneous local metrics remain positive.
The inherited evolution-domain construction and its reflected adjoint extend
unchanged, since the new prime block is a bounded perturbation. For X=V(w,L)
and Z=V(w,h), local energy decay gives the all-input estimates

\[
E=I-X^*X\succeq0.00002999 I,\qquad
F=I-ZZ^*\succeq0.0008795 I. \tag{4.2}
\]

These follow from 1−exp(−2w(m_ell−delta_ell)), not by subtracting projected
output matrices. In particular both inverses in the normalized append exist.

For the complete mixed block,

\[
\begin{split}
\|H_s-H_0\|\le{}&\frac{w^2R^2}{2}\cosh(wR)
\left[\frac\pi2+\sqrt{(e^L-1)(e^h-1)}\right]\\
&+c_p(\cosh(wa)-1)<6.729\,10^{-7}. \tag{4.3}
\end{split}
\]

Here pi/2 is the rectangular Carleman bound for the gamma corner. The signed
growing pole is retained in absolute value for this small perturbation only;
the central mixed operator itself still requires its cancellation.

Define the unknown **complete all-input central** relative norm

\[
\kappa_0=\|Q_{0,h}^{-1/2}H_0Q_{0,L}^{-1/2}\|.
\]

Equations (4.1)–(4.3) and the local floors imply the following useful target:

\[
\boxed{\kappa_0\le0.999\quad\Longrightarrow\quad
\|F^{-1/2}YE^{-1/2}\|<0.99902<1.} \tag{4.4}
\]

The hypothesis of (4.4) is **not proved**. Its implication is checked with
outward rational constants. In detail, sqrt(0.015·0.44)>0.0812, the relative
local losses are below 10^-5 and 3·10^-8, and the mixed perturbation is below
7·10^-7. The uniform relative bound is therefore at most

\[
\frac{0.999+(7\,10^{-7})/0.0812}{1-10^{-5}-3\,10^{-8}}
=\frac{413875000}{414281559}<0.99902.
\]

Apply the existing forward/backward energy-transfer lemma to obtain (4.4).
The beta history, both pole states, and prime echo must still pass across the
join. The reduction does not replace them by reset local systems.

## 5. Certified obstruction to treating the prime as a separate norm cost

On (0,3/4), take the unnormalized real function

\[
\psi(x)=\cos\frac{\pi x}{R}
-\frac{27}{100}\cos\frac{3\pi x}{R}
-\frac1{10}\cos\frac{5\pi x}{R}
-\frac{56}{1000}\cos\frac{7\pi x}{R}.
\]

Its ordinary squared norm is 0.4072635. The rational enclosures, rounded
outward here for readability, give

\[
-0.001003<Q^A_{0,R}[\psi]<-0.000754,
\]
\[
0.021101<Q_{0,R}[\psi]<0.021350.
\]

The exact prime contribution is approximately +0.02210390116. It equals

\[
-\sqrt2\log2\int_0^{R-a}\psi(x+a)\psi(x)\,dx,
\]

whose overlap integral is negative. The sign change is therefore a genuine
signed arithmetic contribution, not an output normalization change.

Since both diagonal local forms are positive by Section 3, the first inequality
and the block identity imply
\(\|Q_{0,h}^{-1/2}H_0^A Q_{0,L}^{-1/2}\|>1\).
Any triangle-inequality upper bound that pays this whole archimedean norm
before adding a nonnegative prime norm cost is necessarily above one. This
closes that particular estimation strategy. It does not exclude a bound for
the sum, a different decomposition, or cumulative storage.

The positive complete value is a **single-input result**. It does not establish
positivity of the complete form on all inputs.

## 6. Certified failure of the M=128 proxy, with a positive complete control

In the reflected old and physical new coordinates use the rational functions

\[
f(r)=1.061+0.842\cos(\pi r/L)-0.271\cos(2\pi r/L),
\]
\[
v(t)=0.809+0.592\cos(\pi t/h)+0.014\cos(2\pi t/h).
\]

Their combined ordinary squared norm is 1.000270125. Retain the **complete**
mixed H_0, but replace the diagonal forms by their physical M=128 truncations.
The certificate proves

\[
-0.004133< T_{128,L}[f]+T_{128,h}[v]
-2\Re\langle v,H_0f\rangle<-0.003380. \tag{6.1}
\]

For precisely the same functions, the complete form satisfies

\[
0.004951< Q_{0,L}[f]+Q_{0,h}[v]
-2\Re\langle v,H_0f\rangle<0.006525. \tag{6.2}
\]

These are rational inequalities for the full specified functions, not signs
inferred from a floating eigenvector. The witness coefficients were selected
using floating exploration, then fixed as rationals before certification.

The truncated diagonal operators are positive by Section 3. Hence (6.1)
proves that their exact relative coupling exceeds one. Replacing them by
still smaller metrics, including the previous head/complement lower metrics,
cannot repair this failure. It is already present on three modes per side;
finer resolution of the **same** lower operator is not the missing result.

The scope matters: the obstruction applies to this M=128 pointwise-energy
proxy. It does not exclude a larger or differently organized lower operator,
the complete metric, or an estimate using cumulative cancellations in shift.

### How the infinite series and witnesses are enclosed

The local witness energies retain 4096 gamma terms with exact rational
coefficients and outward exp/pi bounds. For a cosine polynomial g on (0,ell),
zero-extended outside that interval, the translation difference satisfies

\[
\|g\|^2-\Re\langle g,S_u g\rangle
\le u\|g\|_\infty^2+\frac{u^2}{2}\|g'\|^2.
\]

This follows by treating the two endpoint strips separately and applying
Cauchy–Schwarz to the interior difference. It also proves finiteness of the
gamma form for these tests; no endpoint terms are dropped. Consequently the
positive omitted local gamma energy is at most

\[
2\|g\|_\infty^2\sum_{n\ge M}a_n^{-2}
+2\|g'\|^2\sum_{n\ge M}a_n^{-3}. \tag{6.3}
\]

Use the coefficient-sum bound on the supremum norm and the exact cosine
derivative norm. Decreasing-series integral bounds give, with A=2M+1/2,
\(\sum a_n^{-2}\le A^{-2}+(2A)^{-1}\) and
\(\sum a_n^{-3}\le A^{-3}+(4A^2)^{-1}\).

For the mixed archimedean pairing, retain the exact exponential series from
n=1 to 4096 and bound its remainder by
\(\|f\|_\infty\|v\|_\infty\sum_{n>4096}a_n^{-2}\).
The growing pole is an exact separate term. Prime pairings are integrated
analytically as cosine products, with outward trigonometric intervals.
Section 6.1 of the inherited certificate supplies the local cosine matrix
identity; no conjectural arithmetic sign enters these witness estimates.

## 7. Complete-form diagnostics and what they do not prove

The floating diagnostic uses full local translation-correlation forms and
physical-delay cross-section quadrature for H^A; it integrates the prime
translation on its exact segment. This differs from the certificate's
exponential-series computation and provides a useful reduction check.

| Cosines per local window | Archimedean relative quotient | Prime relative quotient | Complete relative quotient |
|---:|---:|---:|---:|
| 16 | 1.05561291 | 0.62035139 | 0.99610879 |
| 32 | 1.06318136 | 0.63168539 | 0.99641961 |
| 64 | 1.06523924 | 0.63538354 | 0.99647095 |
| 96 | 1.06569010 | 0.63607134 | 0.99647753 |

The 64-mode complete quotient changes by less than 6e−14 in a higher-order
quadrature run. This checks that particular quadrature comparison, not an
error bound on all unrepresented inputs. Eight controls check witness
pairings and signs against the rational enclosures and the repeated quadrature.

At fixed 32-mode heads the lower-tower relative quotients are approximately
1.04077, 1.01718, 1.00641, 1.00132, and 0.99884 for M=128,256,512,1024,2048.
Increasing M does restore useful gamma energy in this finite test. The final
number is not an all-input bound: the metric cross blocks and both infinite
mixed complements remain to be controlled. The exact M=128 obstruction is
stronger evidence than this numerical trend.

No small-shift all-input coupling value is inferred from the table. The table
supports investigating the hypothesis of (4.4); it does not establish it.

## 8. Next steps and their broader value

The immediate problem is now narrower: **prove a complete central relative
bound at most 0.999, retaining enough omitted gamma energy**, or identify a
better cumulative estimate if that route proves too expensive. The local
metrics, shift perturbations, and diagonal inverses are already available.

The next calculation should examine the weak directions of the complete
mixed form and construct a lower energy estimate that retains the gamma tail
they use. Compare a controlled grouped tail with a larger finite tower, keeping
the actual metric cross blocks through a Schur complement rather than spending
the small margin in a coarse scalar loss. For the prime complement, use its
exact partial-translation structure and relative energies; equation (2.1)
precludes simply declaring its omitted norm small. Preserve the signed sum of
gamma, poles, and prime in the sensitive mixed blocks.

This is **high-value methodological work** because it tests whether the parent
continuation method can survive a genuine arithmetic delay. A successful
certificate at R=3/4 would still be a bounded method result inside already
studied positive windows, not a new positivity horizon or evidence of an
all-depth continuation invariant by itself.

For the broader program, the most informative new lesson is that discarding
positive gamma energy can erase the very cancellation needed at a prime
threshold. The Sonin direction should therefore be compared with the complete
metric and its signed remainder, not just an independently positive projected
space. A proved map that restores the missing directional energy would have
greater structural value than another favorable small-window calculation.
The Sonin projection/remainder has not been newly evaluated in this session.

The current transference method still uses positive instantaneous local
metrics and a uniform relative bound. It does not yet solve the genuinely
cumulative problem when those metrics fail. An all-depth invariant or a
storage identity that works beyond that regime remains the higher-impact
long-term target. No new WZW or N4SYM calculation is indicated by this session
unless it supplies a specific state norm or coupling estimate for that gap.

The gamma/pole negative witness is a concrete control in this session. The
broader program's separate negative smooth-density replacement has not been
tested here and remains a required discriminator for a proposed general
arithmetic mechanism.

## 9. Reproduction and evidence ledger

See the [numerics guide](../numerics/README.md) for commands. The new files are:

- [Rational certificate source](../numerics/certify_first_prime_inputs.py), with
  [40-digit](../numerics/records/first-prime-inputs-40digits-20260924.json) and
  [60-digit](../numerics/records/first-prime-inputs-60digits-20260924.json) records.
- [Independent floating reduction source](../numerics/diagnose_first_prime_coupling.py)
  and [diagnostic record](../numerics/records/first-prime-coupling-diagnostics-20260924.json).
- [Record and conditional-implication checker](../numerics/check_first_prime_records.py)
  and [record](../numerics/records/first-prime-record-checks-20260924.json).

Both precision runs passed; all 15 recorded interval pairs are nested at the
higher precision. The conditional implication was checked with exact fractions,
with its unproved hypothesis explicitly marked false as a certification claim.
The eight floating reduction controls passed. Source and dependency hashes
bind the records to the implementations.

These are internal computer-assisted results. Replaying the arithmetic and
cross-checking formulas do not constitute independent specialist review of
the analytical reductions. No old proof, manuscript, or snapshot is replaced.
Only sources, notes, and small records are added under the repository's
large-files policy.
