# A certified positive-time obstruction for the Euler-factor control

14 October 2026. Prepared for Edward Baker with LLM assistance by
`gpt-6-astra` (Codex), reasoning effort **ultra**.

## Result

For the exact parameters
\[
c=\frac12,\qquad p=41,\qquad t=\frac15,
\qquad x=\frac{168413}{100000},
\]
the full, unnormalized Laguerre expression satisfies
\[
\boxed{
-0.000005299994533574706
<\mathscr L_0(H^{1/2,41}_{1/5};x)
<-0.000005299994533574704<0.
}
\tag{2.1}
\]
Consequently, by the Laguerre criterion in
[Note 1, Proposition 2](1_EXACT_FLOW_WITNESSES_AND_ASYMPTOTICS_20261013.md#2-proposition-2-laguerre-witnesses),
\[
\boxed{\Lambda_{1/2,41}>\frac15.}
\tag{2.2}
\]
This is a computer-assisted interval certificate, using Arb through
python-flint. The [checker](../numerics/certify_euler_factor_witness.py)
and [small execution record](../numerics/EULER_FACTOR_WITNESS_RECORD_20261014.json)
are self-contained apart from that arithmetic library. The proof below
supplies the source truncation and infinite-tail bounds; validated
quadrature supplies the finite-integral error. No floating-point candidate
zero, collision time, or normalized ratio enters the sign proof.

The conclusion is one control's positive-time obstruction. It does not
identify a tracked collision with the global Newman constant, establish
an upper bound for that constant, or imply RH.

## 1. An integral with one nonnegative source variable

For \(v\ge0\), set
\[
\Phi(v)=\sum_{n\ge1}
\left(2\pi^2n^4e^{9v}-3\pi n^2e^{5v}\right)
e^{-\pi n^2e^{4v}}.
\tag{2.3}
\]
Let \(\Phi_e\) denote its even extension, put
\(a=\tfrac12\log41\), and use the normalization
\[
\Phi_{c,p}(u)=\Phi_e(u)+\frac c2
\bigl[\Phi_e(u+a)+\Phi_e(u-a)\bigr],\qquad
H^{c,p}_t(x)=\int_0^\infty\Phi_{c,p}(u)e^{tu^2}\cos(xu)\,du.
\tag{2.4}
\]
For \(j=0,1,2\), define
\[
w_j(r)=r^je^{tr^2}\cos(xr+j\pi/2),\qquad
K_j(v)=w_j(v)+\frac c2\bigl[w_j(v+a)+w_j(v-a)\bigr].
\]
Then the exact derivatives are
\[
\boxed{(H^{c,p}_t)^{(j)}(x)=\int_0^\infty\Phi(v)K_j(v)\,dv.}
\tag{2.5}
\]

Indeed, each \(w_j\) is even. Write the half-line integral as half
the whole-line integral, translate each of the two source shifts, and
use evenness to return to \(v\ge0\). Differentiation is justified by
the double-exponential source decay, which dominates the Gaussian and
any fixed polynomial. In code the three trigonometric factors are
\(\cos(xr),-\sin(xr),-\cos(xr)\), respectively.

Thus negative values of \(v-a\) occur only in the entire elementary
factor \(w_j\). The theta series is evaluated at nonnegative \(v\).
Both shifted tails are included in (2.5); a finite cutoff in the source
variable is not a cutoff in the original shifted variable.

## 2. Omitted theta indices on the finite interval

The certificate uses \(U=1\), retains \(n\le N=4\), and puts
\(m=N+1=5\). All summands of (2.3) are positive, since
\(2\pi n^2e^{4v}>3\). For \(n\ge m\), the function
\(9v-\pi n^2e^{4v}\) decreases on \(v\ge0\), because
\(4\pi m^2>9\). Dropping the negative term in (2.3) therefore gives
\[
0\le\Phi(v)-\Phi_N(v)
\le2\pi^2\sum_{n=m}^{\infty}n^4e^{-\pi n^2}
\le B_N:=\frac{2\pi^2m^4e^{-\pi m^2}}{1-q},
\tag{2.6}
\]
where
\[
q=\left(\frac{m+1}{m}\right)^4e^{-\pi(2m+1)}<1.
\]
The consecutive-term ratio is at most \(q\) for every \(n\ge m\).
For \(0\le v\le U\), \(|v|,|v\pm a|\le U+a\), so
\[
|K_j(v)|\le(1+c)(U+a)^je^{t(U+a)^2}.
\]
It follows that the finite-interval source-truncation error is at most
\[
D_j=U B_N(1+c)(U+a)^je^{t(U+a)^2}.
\tag{2.7}
\]
All expressions in (2.6)–(2.7) are evaluated by outward real-ball
arithmetic. The checker verifies their strict inequality hypotheses.

## 3. The complete source and control-shift tail

For \(n\ge1\), \(n^4\le16^{n-1}\) and
\(n^2-1\ge3(n-1)\). Since \(16e^{-3\pi}<\tfrac12\), for
every \(v\ge0\) equation (2.3) yields
\[
0<\Phi(v)
\le2\pi^2e^{9v-\pi e^{4v}}
\sum_{n\ge1}\bigl(16e^{-3\pi e^{4v}}\bigr)^{n-1}
\le4\pi^2e^{9v-\pi e^{4v}}.
\tag{2.8}
\]
For \(v\ge U\), the absolute integrand in (2.5) is bounded by
\[
M_j(v)=(1+c)4\pi^2(v+a)^j
\exp\{9v+t(v+a)^2-\pi e^{4v}\}.
\]
Its logarithmic derivative is
\[
\frac{j}{v+a}+9+2t(v+a)-4\pi e^{4v}.
\]
Its derivative is strictly negative for \(v\ge U\), as follows
from the checked inequality \(16\pi e^{4U}>2t\). The checker also
verifies, for each \(j\in\{0,1,2\}\),
\[
d_j=4\pi e^{4U}-9-2t(U+a)-\frac{j}{U+a}>0.
\]
Hence \(M_j(U+s)\le M_j(U)e^{-d_js}\) for \(s\ge0\), and
\[
\left|\int_U^\infty\Phi(v)K_j(v)\,dv\right|
\le T_j:=\frac{(1+c)4\pi^2(U+a)^j
e^{9U+t(U+a)^2-\pi e^{4U}}}{d_j}.
\tag{2.9}
\]
This bound uses the complete theta series and includes both shifted
control terms. No omitted source or shift tail remains.

## 4. Validated quadrature and the resulting interval

The finite integrals
\(I_j=\int_0^U\Phi_N(v)K_j(v)\,dv\) are evaluated by
`flint.acb.integral` at 128-bit precision. The relative and absolute
tolerance goals are \(2^{-90}\); these are algorithmic goals, not
substitutes for its returned error enclosure. Each callback is entire
in its complex input: only polynomials, exponentials, sine, and cosine
occur. The real constant \(a\) is enclosed before integration. This
satisfies the documented analytic-callback obligation for the
[validated integration interface](https://python-flint.readthedocs.io/en/latest/acb.html#flint.acb.integral).
The checker requires finite returned balls and an imaginary enclosure
containing zero; reality follows independently from (2.5).

For each real returned enclosure, the checker adds a symmetric ball
with radius equal to an outward upper bound for \(D_j+T_j\).
The final jet enclosures, displayed with conservative rounding, are

| Jet | Full enclosure |
| --- | --- |
| \(H\) | \([2.4869490795960836827310757236886959\cdot10^{-5}\ \pm2.98\cdot10^{-29}]\) |
| \(H_x\) | \([-1.2855250161606757416165707245992851\cdot10^{-6}\ \pm7.42\cdot10^{-29}]\) |
| \(H_{xx}\) | \([0.21311237249015439787630545398441803\ \pm2.06\cdot10^{-28}]\) |

For orientation, the three \(D_j\) are less than
\(7.36\cdot10^{-30},2.11\cdot10^{-29},6.01\cdot10^{-29}\),
and the three \(T_j\) are less than
\(1.17\cdot10^{-71},3.34\cdot10^{-71},9.55\cdot10^{-71}\).
The JSON stores the actual outward bounds and exact dyadic endpoints
for each intermediate and final enclosure, rather than relying on
these rounded summaries.

Outward evaluation of \(H_x^2-HH_{xx}\) gives
\[
\mathscr L_0\in
2^{-142}\left[
-29548456911713663386963614654148589637,
-29548456911713663386963543968550828101
\right].
\tag{2.10}
\]
In decimal-ball display this is
\[
[-5.2999945335747050670520276381662228\cdot10^{-6}
\ \pm6.34\cdot10^{-30}].
\]
The checker compares the full ball with zero and with the exact rational
endpoints in (2.1). Both comparisons succeed. No division by \(H^2\)
is used.

## 5. Replay, provenance and scope

Install `python-flint` in the chosen Python environment; version 0.9.0
was used, with Python 3.10.0. From this investigation's `numerics/`:

```sh
python3 -B certify_euler_factor_witness.py --output /tmp/euler-factor-witness.json
```

The script prints the record and exits nonzero unless every bound and
the strictly negative raw sign passes. The retained JSON binds the
checker by SHA-256 and records the exact rational parameters, precision,
cutoffs, arithmetic-library version, intermediate payments, and final
dyadic interval. The hash identifies the executed source; the arithmetic
sign check proves the stated conclusion. No external data files are
required. Exact byte equality of records is not promised across library
versions; a replay must establish the sign using its own enclosures.

A separate replay with `--precision 192 --theta-terms 5` also passed all
bounds and the same rational display bracket. Its raw value agreed with
(2.10), with the narrower ball centred at
\(-5.2999945335747050670520276381688873\cdot10^{-6}\).
That replay is a check on stability; the retained 128-bit record already
proves the sign by its own enclosures.

This completes the one-witness certification gate identified in Note 1.
It is a rigorous failure example for candidate criteria built only from
the structural properties retained by these controls. Further theta
criteria still need to identify and test a property that the control
loses. Broadening numerical collision tables is not needed for this
certificate, and the historical table remains numerical evidence about
tracked branches only.
