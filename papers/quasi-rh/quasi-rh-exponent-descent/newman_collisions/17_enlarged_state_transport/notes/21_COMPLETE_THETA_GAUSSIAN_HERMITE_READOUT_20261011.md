# Complete theta Gaussian Hermite readout for stationary losses

11 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); active reasoning effort is unavailable and is not inferred.
Internal analytic derivation; not independent mathematical validation.

The companion [explicit correction note](20_EXPLICIT_THETA_CORRECTION_AND_CORRELATED_PHYSICAL_JETS_20261011.md) supplies the new effective remainder bound and stationary certificate.

## Result and purpose

The valid Gaussian lift in investigation 17, Note 10, can be reduced to a
one-dimensional, derivative-free readout of the *actual complete* time-zero
theta transform. Four real Gaussian Hermite moments give the four physical
jets needed by the stationary tests exactly. Their signed correlations
translate the proposed bounded-loss criterion without introducing a freely
chosen error or an unspecified complex channel. This is an exact comparator
for a corrected finite-sum computation, not a new positivity theorem.

The resulting positive Gaussian norm is a standard Hermite/heat identity.
Like the manuscript's positive enlarged-state norms, it does not control
the sign or observability of its first few coordinates. No novelty claim is
made for the Gaussian transform or its Parseval identity.

## 1. Exact complete-theta input

Use the manuscript normalization

\[
 H_t(x)=\frac12\int_{\mathbb R}e^{ixu+tu^2}\Phi_e(u)\,du,
 \qquad H_0(z)=\frac18\xi\!\left(\frac{1+iz}{2}\right).
\]

The second equality is Note 10's complete single-factor Mellin identity.
It is the entire completed function, with all theta terms and modular
gluing already included, not a raw divisor-channel continuation.

Fix a real physical point \(x\) and \(t>0\). Let \(Z\) be standard normal,
\(s=\sqrt{2t}\), and

\[
 f_{t,x}(Z)=H_0(x+isZ)
 =\frac18\xi\!\left(\frac{1-sZ+ix}{2}\right).
\]

The actual function is therefore fixed completely by theta data. Gaussian
exponential moments give

\[
 \boxed{\mathbb E f_{t,x}=H_t(x).} \tag{1}
\]

The theta source decays faster than every Gaussian at both real ends, so
Gaussian/source Fubini is justified after taking absolute values. For
example, the two-source majorant for \(\mathbb E|f_{t,x}|^2\) is a constant
times

\[
 \iint |\Phi_e(u)\Phi_e(v)|e^{t(u+v)^2}\,du\,dv<\infty.
\]

Polynomial insertions are harmless. The same domination justifies the
fixed Gaussian integrations by parts used below. No all-line raw Mellin
channel is interchanged with the Gaussian integral.

## 2. Four real Hermite coefficients

Write \(a(Z)=\Re f_{t,x}(Z)\), \(b(Z)=\Im f_{t,x}(Z)\). Conjugation
makes \(a\) even and \(b\) odd. Define

\[
 m_0=\mathbb E a,\quad m_1=\mathbb E[Zb],\quad
 m_2=\mathbb E[(Z^2-1)a],\quad
 m_3=\mathbb E[(Z^3-3Z)b].
\]

For the probabilists' Hermite polynomial \(\operatorname{He}_n\), Gaussian
integration by parts gives

\[
 \mathbb E[\operatorname{He}_n(Z)f_{t,x}(Z)]
 =(is)^nH_t^{(n)}(x).
\]

Consequently the exact physical dictionary is

\[
 \boxed{H_t=m_0,\quad H_t'=m_1/s,\quad
 H_t''=-m_2/s^2,\quad H_t'''=-m_3/s^3.} \tag{2}
\]

No normalizer derivative, contour derivative, or derivative of a numerical
approximation is being suppressed in (2).

Hermite Parseval also gives the exact positive identity

\[
 \boxed{\mathbb E|f_{t,x}|^2
 =\sum_{n\ge0}\frac{(2t)^n}{n!}\bigl(H_t^{(n)}(x)\bigr)^2.} \tag{3}
\]

The Hermite coefficient functions are real or purely imaginary according
to parity. Orthogonality therefore supplies exactly the positive squares
in (3). Completeness applies because the preceding two-source majorant
puts the actual function in Gaussian \(L^2\).

## 3. Exact signed covariance target near a small first jet

Let \(E=H_t^2+(H_t')^2=m_0^2+m_1^2/s^2\). The proposed sufficient
stationary bounds

\[
 HH''\le C_0E\quad(H'=0),\qquad
 H'H'''\le C_1E\quad(H''=0)
\]

become exactly

\[
 m_0m_2\ge-s^2C_0m_0^2\quad(m_1=0), \tag{4}
\]
\[
 \boxed{m_1m_3\ge-s^4C_1(m_0^2+m_1^2/s^2)
 \quad(m_2=0).} \tag{5}
\]

These formulas retain the joint energy in the denominator; they impose no
relative-to-slope requirement at a point where \(H'=H''=0\) but \(H\ne0\).

There is a derivative-free covariance form:

\[
 m_2=\operatorname{Cov}(Z^2,a),\qquad
 m_3=\operatorname{Cov}(Z^2,Zb)-2m_1.
\]

Thus (5) is the following definite complete-xi correlation question:

\[
 m_1\operatorname{Cov}(Z^2,Zb)
 \ge (2-s^2C_1)m_1^2-s^4C_1m_0^2
 \quad\text{when }\operatorname{Cov}(Z^2,a)=0. \tag{6}
\]

This is an exact reformulation of the chosen stationary inequality, not an
independently proved estimate. Its value is that the data are the complete
theta function sampled in a specified Gaussian window, and the required
correlation can be measured without numerically differentiating it.

Gaussian positivity alone proves neither (4) nor (6). In particular, (3)
only bounds the low-order coefficients by the whole norm. Replacing the
needed signed correlation by an unproved upper bound of that whole norm
by \(E\) would reintroduce the enlarged-state observability problem.

## 4. Relation to the fixed-source-contour current route

Note 13's channel \(\mathcal C_a\) remains a valid alternative, with
\(a\) fixed during physical differentiation. Its currents depend on the
chosen imaginary component; the existing real-observation disk does not
bound that component. Equations (1)--(6) instead use the fixed entire
time-zero theta transform and concern only the physical jets. They require
their own rigorous integration/evaluation bounds before numerical use,
but no new complex-channel gauge needs to be estimated.

The half-line endpoint-subtracted channel's current product at genuine
stationarity is algebraically the scalar Laguerre target when its complex
second derivative is nonzero. The exceptional set still needs treatment.
Neither that representation nor this Hermite representation supplies
theta-specific positivity automatically.

## 5. Recommended use and limits

Use (2) as an independent exact-source comparator for the leading explicit
correction to the current finite-sum approximation. For a small set of
physical stationary candidates, compare the four signed Hermite moments
with the corrected physical jets, and track (4)--(6) relative to the joint
energy. All numerical claims require complete-xi evaluation bounds and
Gaussian tail payments; none has been performed in this note.

The main analytic question remains a theta-specific proof of (4) and (5),
or a justified weaker loss rate sufficient for the multiplicities under
consideration. A positive Gaussian norm or a successful large-signal cell
is insufficient. The formula does not settle growing-product transition
asymptotics, uniform stationary signs, collision exclusion, or RH.

Sources within investigation 17: Note 10 Sections 3 and 5 (complete xi
normalization and valid heat lift); Note 7 Sections 1--3 (complete paired
kernels and their sign hierarchy); Note 13 Sections 1, 5 and 6 (current
identity, channel ambiguity, and fixed-contour definition).
