# Stationary survey and certified ambiguity of the coarse disk estimate

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); the active reasoning effort is not exposed to this
session and is not inferred. Exploratory numerics, outward arithmetic and
separate-agent checks are internal LLM work, not independent mathematical
validation.

The small-first-jet survey finds a limitation of the current third-jet
resolution. An outward check then proves that the printed coarse disk
allowance permits opposite stationary signs at the same value and slope
of the actual prescribed finite sum. This is not an adverse stationary
point of the genuine theta function and is not a collision certificate.

## Exploratory survey on connected windows

The [survey source](../numerics/survey_stationary.py) uses
\[
x=4\pi N^2+h,\quad 0\le h\le256,\qquad
t_0=\frac1{2\log N}.
\]
It samples a frozen-frequency locator at spacing \(1/16\), then refines
every detected sign-change bracket with the full physical finite-sum jets.
Even roots or two roots inside one grid interval can be missed. The roots
are those of the finite approximant, not certified stationary points of
the genuine theta flow.

| Scale and time | Detected first stationary roots | Detected second stationary roots | Smallest normalized energy at first roots | Smallest normalized energy at second roots | Second roots passing the naive pointwise sign payment |
| --- | ---: | ---: | ---: | ---: | ---: |
| N=22066, t=t0 | 407 | 408 | 0.197028 | 7.685982 | 43 |
| N=22066, t=t0+1e-8 | 407 | 408 | 0.197028 | 7.685984 | 43 |
| N=100000, t=t0 | 469 | 468 | 0.140374 | 6.486513 | 317 |

Every detected finite stationary product was negative. The first jets
remained separated from their absolute error estimates. These runs do not
identify an incipient joint zero or prove a bounded-loss theorem.

At \(N=22066\), the weakest second stationary point is near offset
58.5690906002, with physical finite normalized jets approximately
\[
(f_0,f_1,f_2,f_3)=(0.0860406,-2.7710249,0,97.6555061).
\]
The imported physical disk errors are approximately
\[
(0.00964146,0.19664994,7.86889518,472.21895989).
\]
The third-jet payment is about 4.84 times the nominal third jet.
At \(N=100000\), the weakest second point is near 181.187030524,
with \(f_3\approx116.170261\), still smaller than its approximately
279.366987 third-jet payment.

These pointwise error comparisons do not enclose genuine root motion.
The column counting nominal successful payments is therefore diagnostic,
not a count of certified theta stationary branches.

The finite physical multipliers are
\[
1,\quad\beta_n,\quad\beta_n^2+\beta_n',\quad
\beta_n^3+3\beta_n\beta_n'+\beta_n'',
\qquad
\beta_n=-\frac i2(\alpha-\log n)(1+t\alpha_s/2).
\]
The code retains normalizer and frequency drift. Base phases use 60-digit
Decimal reduction; sums and root refinement use NumPy floating arithmetic.
The recurrence \(f_j'=f_{j+1}-\lambda f_j\), \(j=0,1,2\), was checked
by finite differences at three separated offsets per run. The recorded
root residuals were below \(10^{-10}\). A replay with the final source
reproduced all 815 first-run root tuples exactly in the same environment.
Neither check turns the floating survey into a proof.

## A rigorous ambiguity at the actual finite-sum point 58.57

Fix
\[
N=22066,\quad t=t_0,\quad x=4\pi N^2+58.57,\quad
L=\log(x/(4\pi)),\quad \eta=5e^{-tL^2/16-L/4}.
\]
Let \(G=AF\) be the complete prescribed finite reflected approximant,
and \(f_j=G^{(j)}/A\), with physical derivatives. The
[outward checker](../numerics/check_stationary_disk_ambiguity.py)
regenerates all 22,066 terms and gives the following rounded-outward
enclosures, including its finite spatial transport errors:
\[
\begin{aligned}
0.08352389&<f_0<0.08357718,\\
-2.77201612&<f_1<-2.77193246,\\
0.08869167&<f_2<0.08888916,\\
97.58406371&<f_3<97.58468538.
\end{aligned}\tag{1}
\]
These are enclosures of the finite approximant; the independent Cauchy
error boxes are separately recorded.

Put \(w=L(z-x)\) and define the two analytic observations
\[
H_\pm(z)=G(z)+A(z)\eta(a_2w^2\pm\tfrac12w^3),
\qquad a_2=-\frac{f_2}{2\eta L^2}.
\tag{2}
\]
The coefficient uses the exact finite \(f_2\), enclosed by the checker.
It has
\[
-0.01152021<a_2<-0.01149461,\qquad
|a_2|+\tfrac12<0.511521<1.
\tag{3}
\]
Both observations therefore lie strictly inside the printed coarse
normalized disk allowance on \(|z-x|\le1/L\).

At the center their value and slope equal those of \(G\), and their
second derivatives vanish exactly. The normalizer contribution is essential:
\[
\frac{H_\pm'''(x)}A=f_3-3\lambda f_2\pm3\eta L^3,
\qquad\lambda=A'/A.
\tag{4}
\]
The outward result proves
\[
-133.83097<\frac{H_-'''}A<-133.83010,
\qquad
329.20806<\frac{H_+'''}A<329.20893.
\]
Since the common slope is negative, the minus observation has the adverse
stationary product and the plus observation has the favorable product:
\[
370.96802<\frac{H_-'H_-'''}{A^2}<370.98159,
\]
\[
-912.57244<\frac{H_+'H_+'''}{A^2}<-912.54252.
\tag{5}
\]
Their common first-jet energy satisfies
\[
7.69058584<f_0^2+f_1^2<7.69105848.
\]
The corresponding product/energy ratios lie in
\((48.23367,48.23841)\) and \((-118.66098,-118.64979)\).
Thus even exact knowledge of these lower jets, together with the printed
coarse disk control, cannot force the stronger second stationary sign.

This uses the allowed envelope \(\eta=5e^{-tL^2/16-L/4}\), not a claim
that it is the smallest valid error bound. A sharper proved remainder or
additional theta-specific correlation could distinguish the observations.
The genuine theta function is not identified with either alternative.

## Heat compatibility and the precise limitation

An arbitrary analytic spatial observation need not admit an analytic
backward heat evolution across the reference time. No direct
Cauchy–Kowalevski assertion in time is used here.

There is nevertheless a valid local heat realization. The observations
(2) are holomorphic on a neighborhood of the closed disk and have strict
slack in (3). Taylor polynomials about \(x\) approximate them uniformly
on a slightly larger disk. Truncations of degree at least three preserve
their first four center jets exactly. Choose a sufficiently high truncation
to retain the strict normalized disk slack. Its finite polynomial heat
evolution
\[
P_t(z)=\sum_{j=0}^{\lfloor\deg P/2\rfloor}
\frac{[-(t-t_0)]^j}{j!}P^{(2j)}(z)
\]
solves \(\partial_tP_t=-\partial_z^2P_t\) and remains in the prescribed
tube on a sufficiently small neighborhood by uniform continuity. A slightly
larger disk handles nearby centers and radii. This is the same mechanism
proved in [Note 18](18_CORRELATED_ERROR_JETS_AND_LOCAL_HEAT_AMBIGUITY_20261010.md).

The example does not refute the bounded-loss criterion: its first-jet
energy is separated from zero, so its adverse ratio is finite. It also
does not exhibit collision ambiguity at this center. Note 18 proves the
separate general collision-ambiguity result for strict interior first-jet
candidates; the present center is not such a candidate.

## Records and reproduction

The [small survey summary](../numerics/STATIONARY_SMALL_JET_SURVEY_RECORD_20261010.json)
retains all run parameters, counts, weakest rows, derivative validations,
source hashes, raw-output hashes and canonical root-array hashes. Full root
arrays are regenerable sweep output and are not added to the repository.
Run from this investigation's numerics directory, choosing an output outside
the repository:

```sh
python3 survey_stationary.py --N 22066 --record /tmp/project17_survey_n22066.json
python3 survey_stationary.py --N 22066 --time-shift 0.00000001 --record /tmp/project17_survey_n22066_tplus.json
python3 survey_stationary.py --N 100000 --record /tmp/project17_survey_n100000.json
```

NumPy is the only nonstandard dependency. Canonical root hashes omit timing;
cross-platform floating arithmetic need not reproduce them bit for bit.
No proof depends on those hashes.

The [outward ambiguity record](../numerics/STATIONARY_DISK_AMBIGUITY_RECORD_20261010.json)
is regenerated using only the standard library and the two hash-checked
retained interval sources:

```sh
python3 check_stationary_disk_ambiguity.py
```

Use `--record PATH` only to save a new result. The checker uses four
frozen Taylor moments and evaluates exactly at offset zero, so
each Taylor remainder through derivative three vanishes; finite transport
costs remain fully paid. The directed record reports PASS.

The next source estimate must constrain the actual remainder or its signed
response, rather than treating every holomorphic perturbation under the
coarse envelope as possible. These results add a method obstruction and
an error-analysis interface, not a genuine theta sign or RH conclusion.
