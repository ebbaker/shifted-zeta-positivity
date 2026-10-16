# Continuation: review manuscript and the next arithmetic-depth target

9 September 2026. This is the handoff after writing the new research result as
a paper for review. No computation at the next horizon has been completed in
this turn.

## 1. What to carry forward

The minimal complete handoff is:

1. `FINITE_HORIZON_WEIL_REVIEW_20260909.pdf` -- the 14-page review manuscript
   (check the delivered PDF's actual page count if later revisions change it).
2. `FINITE_HORIZON_WEIL_REVIEW_PACKAGE_20260909.zip` -- editable LaTeX and
   bibliography, the compiled manuscript, this guide, and the complete
   direct-Arb numerical supplement.
3. This continuation guide, if the next conversation needs a short entry point.

Inside the review package, begin with `manuscript/finite_horizon_weil.tex`
or its PDF. The numerical implementation is under `numerics/`.
Its detailed research report and README are retained. The earlier
`DEPTH_1P8_SUPPLEMENT_20260909.zip` contains the same numerical research
packet and is sufficient for continuing calculations if the review package
is unavailable.

The older papers and second-slab archive are useful for historical context,
larger-shift work, or audit work. They are not numerical inputs to the new
central certificate. The first-slab manuscript has outstanding audit
qualifications; do not treat its original numerical presentation as already
independently validated.

## 2. Main result, with exact conventions

Total input horizon is **L**, not a half-width. The centered input interval is
`(-L/2,L/2)`, and the autocorrelation is supported in `[-L,L]`.
Suzuki's multiplicative cutoff is `a=exp(L/2)`.

The new full-operator working certificate is

\[
Q_{0,9/5}\succeq10^{-26}I.
\]

It uses 128 total Legendre modes (degrees 0 through 127), hence 64 in each
reflection sector, a degree-180 analytic profile, and 1536-bit Arb arithmetic.
The gamma logarithmic part is exact. The profile truncation and the infinite
tail are handled analytically.

Both ball LDL tests pass, and replay from the saved matrix enclosures also
passes. The numerical certificate does not use any zeta-zero input, first-slab
matrix archive, external compact-window certificate, or extrapolated Decimal
rounding allowance.

The analytic continuation estimate gives

\[
\|V_{\omega,L}\|\le e^{-5\times10^{-27}\omega},
\qquad 0<\omega\le3\times10^{-14},\quad 0<L\le9/5.
\]

It also gives `I +/- H >= (1-exp(-5e-27 omega)) I`, with `H=V R`, and for any
spatial split `V=[[X,0],[Y,Z]]`,

\[
I-X^*X-Y^*(I-ZZ^*)^{-1}Y\succeq(1-e^{-10^{-26}\omega})I.
\]

These are computer-assisted mathematical claims presented for independent
review. They are not an all-depth result, proof-assistant formalization,
completed external audit, or RH conclusion.

## 3. Why the previously failed calculation now passes

| Quantity at L=1.8 | 96 modes | 128 modes |
|---|---:|---:|
| Analytic scalar tail floor | 0.3921290267 | 0.6912470843 |
| Required floor, even diagnostic | 0.55845 | 0.4905447626 |
| Required floor, odd diagnostic | 0.54762 | 0.4795714956 |
| Full test at central floor 1e-26 | Not certified | Pass |

The required floors are diagnostic largest eigenvalues of the head-relative
coupling. The sign decisions instead use direct ball LDL after analytic
remainder subtraction. A failed sufficient inequality is not a negative
direction of the actual operator.

At 128 modes, the profile norm error is below `2.477e-40`, the total analytic
Schur-model error is below `9.908e-36`, and the largest saved matrix radius is
below `9.341e-215`. The minimum LDL pivots are approximately `5.67963e-5`
(even) and `1.81707e-4` (odd). These pivots are not spectral lower bounds.

The previous code explicitly restricted its aggregate arithmetic budget to
N<=96. That restriction was not simply removed. The new code constructs all
coefficients, moments, matrix products, and final LDL operations in Arb.

## 4. Analytic structure to preserve

The transfer contains all integer layers below exp(L), with coefficients

\[
b_\omega(n)=n^{\omega-1/2}\prod_{p\mid n}(1-p^{-2\omega}).
\]

Its exact symmetric logarithmic generator is

\[
Q_{\omega,L}=Q^\gamma_{\omega,L}
-\sum_{\log n<L}\frac{\Lambda(n)}{\sqrt n}\cosh(\omega\log n)
(T_{\log n}+T_{\log n}^*).
\]

At L=1.8 the generator indices are 2,3,4,5. The transfer also includes n=6.
The reflected full-output Gram includes ordered delay overlaps `(2,2)`,
`(2,3)`, `(3,2)`. The generator has no n=6 term because Lambda(6)=0.

The central gamma derivative is the logarithmic fractional derivative plus
causal convolution by `(G0(t)-1)/t`, where

\[
G_0(t)=e^{t/2}t/\sinh t-4t\cosh(t/2).
\]

The fractional estimate for the entire Legendre tail is

\[
\|I_\nu(I-P_N)\|\le (L/2)^\nu
\sqrt{\Gamma(N+1-\nu)/\Gamma(N+1+\nu)},\quad0<\nu<1.
\]

Differentiating its squared norm inequality at zero gives the central tail
floor. The manuscript now explicitly proves polynomial form-core density;
do not replace an operator-tail estimate by estimates on individual modes.

For the model derivative Utilde, retain the full-output Grams
`F=P Utilde* Utilde P` and `C=P Utilde* R Utilde P`.
For input parity r, the central leakage is exactly

\[
E_r=(F_r+rC_r)/2-q_r^2.
\]

The sufficient matrix test at a positive target m is

\[
(a-m)(q_r-mI)-E_r-\epsilon I\succeq0,
\quad \epsilon=(|a-m|+40000)\eta_M+2\eta_M^2.
\]

The constant 40000 uses the checked full Gram trace bound below 1e7, hence
`||Utilde P||<10000`. Every new run must retain the trace check and the
correct analytic profile remainder. Use outward lower a and outward upper
eta/epsilon; check both parities.

The uniform Cauchy radius 3 is valid for L<3. It yields

\[
\eta_M=256(L/3)^{M+1}/((M+1)(1-L/3)).
\]

Finite arithmetic enclosure does not eliminate this analytic remainder.

## 5. What the paper-writing pass added

The review manuscript has self-contained definitions, a normalized central
Fourier form, proof of the polynomial form core, finite Euler-product generator
derivation, common-domain energy argument, fractional infinite-tail proof,
exact-parity Schur reduction, explicit moment formulas, and a claim-to-code
review map. It isolates the numerical result as a computer-assisted theorem.

It also states and proves the diagonal all-depth observation: exact
contractions along L_j -> infinity and omega_j -> 0 imply central Weil
positivity on every compact smooth test, by compression to a fixed horizon
and a scalar zero-shift derivative. No fixed positive shift interval is needed.
The required infinite sequence has not been constructed.

The bibliography was checked against primary sources. In particular, the
current version 2 of arXiv:2608.24827 is attributed to **Xuefeng Zhu** and has
an updated title. The older version 1 appeared under a different author name;
use the version-2 metadata when citing the latest work. Its reported total
support length 1.6 corresponds to half-width 0.8; our 1.8 is a total length.
None of its numerical results is assumed in the new certificate.

## 6. Next concrete target: total horizon log(7)

The next research task is to certify Q_(0,log7) with the new Arb engine, then
derive an appropriate small-shift interval. At the exact endpoint log(7),
the n=7 delay vanishes almost everywhere. The active generator indices are
still 2,3,4,5. A strict horizon above log(7) activates the next prime.

Suggested sequence:

1. Use a new output directory. Compute the analytic tail floor and profile
   error for the intended N and M before deciding that the model can resolve
   the desired central margin.
2. Try the same exact-parity construction. A reasonable *initial experiment*,
   not a prediction of success, is N=128, M=220, 1792-bit arithmetic, and a
   provisional target floor 1e-34.
3. If the head is positive but the full Schur inequality fails, inspect the
   head-relative coupling before enlarging N to 160 or 192. Increase M if
   the analytic remainder consumes the weak margin. Increase precision if
   finite ball radii or LDL divisions become limiting.
4. If the sufficient inequality passes, derive the new C_L bound and choose
   the shift radius by an exact rational inequality. Do not reuse the 1.8
   continuation constants automatically.
5. If increasing N does not efficiently close the estimate, investigate a
   structured tail inverse or relative remainder instead of repeating a blind
   escalation of dimension.

Example build command, from the numerical directory:

```bash
python certify_arb.py --N 128 --M 220 --bits 1792 \
  --log-horizon 7 --floor 1e-34 --output output/log7_N128
```

Important: `analyze_certificate.py` currently contains rounded-bound and
continuation assertions specific to L=9/5. Generalize those assertions before
using it at log(7). Its relative-coupling routine can be reused, but its
default C<11, shift, and decay constants cannot simply be carried over.

The builder's strict arithmetic-threshold guards are already suitable for a
logarithmic endpoint: integer comparisons handle threshold equality, and
rational-horizon uncertain comparisons fail closed.

## 7. Other project results and unresolved items

| Earlier result | Current status |
|---|---|
| Central coercivity through log(4), floor 5e-13 | Earlier working certificate with its stated Decimal budget; stronger than merely compressing the new 1e-26 floor |
| Central coercivity through log(5), floor 1e-18 | Earlier working certificate with its stated Decimal budget |
| Small-shift contraction through log(3), cutoff 4e-5 | Analytic consequence of the earlier endpoint certificate, with inherited qualifications |
| Second-slab interior contraction [0.05,0.3] | Earlier certificate chain; not rerun during the present paper-writing pass |
| Gap from 4e-5 to 0.05 on the complete second slab | Still open |
| First-slab corrected primary-Arb audit | Still separate and unresolved in the carried record |
| Storage induction using only the preceding slab | Not proved |
| All-depth positivity, global innerness, or RH | Not proved |

The new paper intentionally does not make the earlier numerical chains
dependencies of its principal theorem. Reviewers can evaluate the direct-Arb
result independently. Keep the wider project archives if returning to those
other targets.

## 8. Suggested prompt for the next research conversation

Continue from the attached review manuscript and its numerical supplement.
Target the central Weil form at total horizon L=log(7), using the standalone
Arb implementation and exact reflection-parity full-output coupling. Preserve
the analytic infinite tail and degree-M profile remainder. Start with a
justified precision/model budget, adapt the retained dimension based on the
head-relative coupling, and distinguish a positive finite head from a complete
operator certificate. If positivity is certified, derive the corresponding
small-shift contraction and storage bounds using new horizon-specific
constants. Do not infer an all-depth theorem or close the second-slab shift
gap without additional proof. Record all changes and reproducible results.
