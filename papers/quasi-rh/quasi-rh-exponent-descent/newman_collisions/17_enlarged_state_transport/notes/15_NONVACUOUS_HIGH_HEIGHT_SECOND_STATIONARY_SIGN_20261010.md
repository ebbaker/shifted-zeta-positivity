# A nonempty high-height branch with the second stationary sign

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); active reasoning effort is not exposed and is not
inferred. Internal interval computation and LLM review are not independent
mathematical validation.

## Result and scope

Conditional on the manuscript's complete holomorphic disk approximation,
the second stationary sign is strictly favorable on a nonempty genuine
high-height branch. Put
\[
N=22066,\qquad t_0=\frac1{2\log N},\qquad x_0=4\pi N^2,
\]
and consider
\[
t_0\le t\le t_0+10^{-8},\qquad
x_0+87.38\le x\le x_0+87.44. \tag{1}
\]
For every time in (1), there is exactly one genuine zero of \(H_{xx}\)
in the spatial interval. It lies in \(x_0+[87.400,87.425]\), and there
\[
\boxed{\frac{H_xH_{xxx}}{A^2}<-13941.95,\qquad
\frac{\mathscr L_1(H)}{A^2}>13941.95.} \tag{2}
\]
Here \(A=\exp(\Re m_t)>0\) is the physical normalizer, and the equality
\(\mathscr L_1=H_{xx}^2-H_xH_{xxx}=-H_xH_{xxx}\) uses genuine
stationarity of \(H\), not stationarity of its finite approximation or
normalized observation.

The [checker](../numerics/check_high_stationary_s1_cell.py) and
[small outward record](../numerics/HIGH_STATIONARY_S1_CELL_RECORD_20261010.json)
regenerate all 22,066 terms with 60-digit directed Decimal arithmetic.
Floating-point exploration selected the region; no floating-point value
is used by the certificate.

This resolves a bounded calibration question left by [Note 6](6_PAID_GENUINE_THETA_STATIONARY_SIGNS_20261010.md):
the complete third-jet cost can be paid on a nonempty high-height
\(H_{xx}=0\) branch. The earlier high rectangle had no such branch.
It does not resolve the uniform sign problem or extend collision-exclusion
coverage, since \(H_x\) is already separated from zero throughout (1).

## 1. Domain and imported analytic interface

Numerically, the interval has
\[
0.04999103540096768<t<0.04999104540096769,
\]
\[
6118670944.1043<x<6118670944.1644.
\]
The outward check verifies \(0<t<0.05\), \(1\le \kappa=tL\le1.5\),
\(L=\log(x/(4\pi))\), and
\[
N^2\le x/(4\pi)+t/16<(N+1)^2.
\]
Thus the natural cutoff is fixed throughout the rectangle. The imported
approximation is the complete reflected sum \(F=G_{t,N}/A\), with
\(Q=H/A=F+e\) and
\[
|e(z)|\le\eta,\quad |z-x|\le1/L,\qquad
\eta\le 5e^{-tL^2/16-L/4}. \tag{3}
\]
It is assumed at every physical center in (1), with the cutoff frozen
on each disk. This computation does not prove (3).

Cauchy's estimate gives \(|e^{(j)}|\le j!L^j\eta\) for \(0\le j\le3\).
The physical derivatives additionally include the normalizer. With
\(\lambda=A'/A\),
\[
\begin{aligned}
K_0&=Q,\\
K_1&=Q'+\lambda Q,\\
K_2&=Q''+2\lambda Q'+(\lambda^2+\lambda')Q,\\
K_3&=Q'''+3\lambda Q''+3(\lambda^2+\lambda')Q'
       +(\lambda^3+3\lambda\lambda'+\lambda'')Q,
\end{aligned}\tag{4}
\]
where \(K_j=H^{(j)}/A\). Every term of (4) is retained.

Rounded upward bounds on the errors from (3), after (4), are

| Physical normalized jet | Complete disk error bound |
| --- | ---: |
| \(K_0\) | \(0.00964146\) |
| \(K_1\) | \(0.196650\) |
| \(K_2\) | \(7.868896\) |
| \(K_3\) | \(472.218960\) |

These are supplemented by finite-sum transport and Taylor errors.
They are not replaced by a leading-wave or frozen-frequency estimate.

## 2. Finite-sum enclosure

The checker regenerates spatial moments through order eleven about the
new frozen center \(x_0+87.41\). It uses the exact phase reduction at
\(x_0=4\pi N^2\), followed by interval trigonometry. It does not transport
the earlier midpoint's finite Taylor polynomial across the 87-unit gap.

The spatial difference between the frozen model and the physical sum
is bounded on all of \(x_0+[0,87.44]\). The maximum individual logarithmic
derivative residual is below \(3.594705\cdot10^{-9}\), and its exponential
transport is retained. Time variation is paid across \(10^{-8}\), with
all mixed derivatives through the third spatial jet. The bounds on
finite transport for the real part of one travelling sum, before the
factor two and the normalizer dictionary, are respectively
\[
0.000051620,\quad 0.000056650,\quad
0.000118126,\quad 0.000337520.
\]
The absolute twelfth frequency moment is below \(389460086\); its
Taylor remainder is paid separately for each derivative.

Twelve subintervals of width \(0.005\) cover the spatial rectangle.
Their fully paid union gives
\[
-46.194<K_1<-44.407,\qquad
298.863<K_3<1265.784. \tag{5}
\]
The second derivative at the left and right spatial endpoints satisfies
\[
-31.867<K_2(t,x_0+87.38)<-16.127,
\]
\[
15.242<K_2(t,x_0+87.44)<30.982. \tag{6}
\]
All endpoints displayed in (5)--(6) are rounded outward.

Since \(A>0\), (5) proves \(H_{xxx}>0\). Therefore \(H_{xx}\) is strictly
increasing in \(x\), although the normalized quantity \(K_2\) need not be.
The endpoint signs (6) prove existence and uniqueness of an \(H_{xx}\)
zero for each time. The five subintervals whose paid \(K_2\) enclosures
contain zero give the narrower candidate band and product bound (2).
At the actual stationary points, division is permitted after (5) has
separated \(H_x\) from zero, giving the additional diagnostic
\[
6.65739<-\frac{H_{xxx}}{H_x}<28.06317. \tag{7}
\]
The proof does not use this quotient to handle potential multiple zeros.

## 3. Relation to the analytic continuation

[Note 12](12_EXACT_CARRIER_DEFECT_AND_CUTOFF_EDGE_MASS_20261010.md)
exhibits the exact signed carrier defect and proves why absolute
coefficient masses do not supply a fixed asymptotic margin.
[Note 13](13_PHASE_CURRENTS_RELATIVE_CONES_AND_BANDWIDTH_OBSTRUCTION_20261010.md)
states a sufficient relative phase criterion, including its degenerate
sets. The present rectangle confirms that a fully paid sign can survive
in the actual prescribed sum despite the large absolute third-jet cost.
It supplies neither of those relative estimates near a vanishing slope.

The next analytic question is the correlation of the complete signed
defect with the physical slope, conditional on \(H_{xx}=0\), uniformly
in an unbounded part of the shrinking sector. Its estimate must remain
meaningful as the slope tends to zero. Selected branches with a large
separated slope do not answer that question.

No predecessor neighborhood below the lower time edge of (1) is provided.
The open-domain stationary-sign collision criterion consequently cannot
be promoted to a new closed-domain coverage statement from this rectangle.
There is no RH implication from the bounded calibration.

## Replay

From this investigation's numerics directory:

~~~bash
python3 check_high_stationary_s1_cell.py
~~~

This recomputes and prints the result without overwriting the retained
record. Use the --record option to save a new record. The two retained
interval sources in program 13 are checked against their SHA-256 hashes
before import; the result records the checker's own hash and complete
budgets. Only Python's standard library is required. The recorded run took
about 40 seconds locally; runtime is not mathematical evidence.
