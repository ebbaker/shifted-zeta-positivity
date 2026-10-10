# Eisenstein extraction, the heat commutator, and the spectral slice

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are unavailable and are not inferred. The accompanying review is internal
LLM checking, not independent mathematical validation.

This implements direction 07 of [Heat Note 14](../../notes/14_DIMENSIONAL_REDUCTION_AND_SUPERSYMMETRIC_HEAT_PROGRAM_20261010.md).
The scout gives an exact zero-time coefficient extraction of `xi`, computes
the completion and cusp-gauge commutators with spectral heat, and finds a
second obstruction: the modular spectral slice extracting `xi` on its
critical line is not the unitary scattering slice. Positive modular flux
therefore cannot be invoked for that extracted channel.

## 1. Exact coefficient extraction

Use the completed modular Eisenstein constant term

\[
a_0(y,\sigma)=\Lambda_R(2\sigma)y^\sigma
 +\Lambda_R(2-2\sigma)y^{1-\sigma},\qquad
\Lambda_R(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s).
\tag{1}
\]

Equation (1) and the completion convention are the imported statements
from [Lagarias–Suzuki, equations (10)–(11)](https://arxiv.org/html/math/0412039).
Their positivity and zero theorems concern their stated integrals. The
following extraction is a direct calculation from (1), not an application
of those zero theorems.

Put `s=2 sigma`, `D_y=y partial_y`, and `c(s)=s(s-1)/2`. At a fixed
cusp height `y>1`, define

\[
\mathcal E_s a_0
=\frac{s}{2}y^{-s/2}(D_y-1+s/2)a_0(y,s/2).
\tag{2}
\]

The differential factor annihilates the outgoing power. On the incoming
power it gives `(s-1)Lambda_R(s)y^{s/2}`. Consequently

\[
\mathcal E_s a_0=c(s)\Lambda_R(s)=\xi(s).
\tag{3}
\]

The identity holds meromorphically and its right side is entire. Exceptional
values where exponents coincide or coefficients have poles are interpreted
by this continuation, not by dividing a measured zero by `s-1`. Formula
(2) retains the completion polynomial without a singular denominator.
The constant term can first be obtained by integration over the closed
horocycle; nonconstant Fourier modes are thereby removed. This operation
requires the Eisenstein family and its parameter derivatives as generalized
waves, not square-integrable eigenstates.

Take the heat coordinate

\[
s=\tfrac12+ix/2,\qquad
\Xi_t(s)=8H_t(-2i(s-1/2)).
\]

The exact equation is
`partial_t Xi_t=(1/4) partial_s^2 Xi_t`, with `Xi_0=xi`. Increasing time
is forward heat in the entire variable `s`; it remains backward heat in
the real `x` coordinate. A scattering ratio such as
`Lambda_R(2sigma-1)/Lambda_R(2sigma)` is a different readout.

## 2. Completion and heat do not commute

On a simply connected spectral neighborhood avoiding the poles of
`Lambda_R`, compare the first tangents of two procedures: heat the
uncompleted incoming coefficient and then multiply by `c`, or first
complete it and apply the genuine heat generator. Their difference is

\[
\frac14\partial_s^2(c\Lambda_R)
 -\frac14c\partial_s^2\Lambda_R
=\frac14\big((2s-1)\Lambda_R'+\Lambda_R\big).
\tag{4}
\]

This is not identically zero. Multiplication by the completion polynomial
after spectral heat therefore leaves an explicit unmatched term, already
at the first time derivative. This local tangent calculation does not
define a Gaussian heat semigroup on the meromorphic uncompleted coefficient;
an unrestricted real spectral convolution would cross its poles.

A globally entire incoming cusp field can instead be defined by

\[
V_0(s,q)=e^{qs/2}\xi(s),\qquad q=\log y.
\]

Its readout is `R_q V=e^{-qs/2}V`. If its proposed bulk generator is
`(1/4)partial_s^2`, then exact conjugation gives

\[
\partial_t(R_qV)
=\tfrac14(\partial_s+q/2)^2(R_qV)
=\tfrac14\partial_s^2(R_qV)+\tfrac q4\partial_s(R_qV)
 +\tfrac{q^2}{16}(R_qV).
\tag{5}
\]

The unaccounted drift and multiplication vanish only at the formal port
`y=1`. The actual matching construction is

\[
V_t(s,q)=e^{qs/2}\Xi_t(s),\qquad
\partial_tV_t=\tfrac14(\partial_s-q/2)^2V_t.
\tag{6}
\]

It is an exact incoming-coefficient lift with a declared nongeometric
spectral generator. It is not a deformation of the modular Laplacian.
For compact `q` ranges, the entire `xi` coefficient has sub-Gaussian growth
along real spectral translates, so the Gaussian spectral heat representation
of (6) is legitimate. Alternatively, the full theta integral defines it
directly without a convolution-domain assumption.

## 3. The eigenwave and physical-slice obstructions

For the positive modular Laplacian, an Eisenstein family at `sigma=s/2`
has eigenvalue

\[
\lambda(s)=\tfrac s2-\tfrac{s^2}{4}.
\]

Differentiating `(Delta-lambda)E=0` twice gives

\[
(\Delta-\lambda)\partial_s^2E
 =(1-s)\partial_sE-\tfrac12E.
\tag{7}
\]

Thus a heat tangent `(1/4)partial_s^2E` has eigenwave residual
`(1-s)partial_s E/4-E/8`. Its incoming cusp term is not zero as a
function of cusp height: spectral differentiation inserts `q/2` into the
power `exp(qs/2)`. At `s=1`, the surviving `-E/8` is already nonzero.
Spectral heat consequently mixes eigenwaves and their derivatives; a
fixed-eigenvalue Maass–Selberg identity cannot be reused unchanged.
Ordinary geometric heat `exp(-t Delta)` instead multiplies a fixed
eigenwave by `exp(-t lambda)` and does not implement (6).

There is an earlier mismatch for a positive-flux interpretation. On the
genuine real-height readout, `s=1/2+ix/2`, the selected modular parameter is
`sigma=1/4+ix/4`, and

\[
\lambda=\frac{3+x^2}{16}+i\frac{x}{8}.
\tag{8}
\]

For nonzero `x`, this is not a real spectral energy of the positive
self-adjoint Laplacian. The standard unitary scattering slice is
`Re sigma=1/2`, which would extract `xi(1+2ik)`, not the required
critical-line `xi`. Meromorphic coefficient extraction remains valid on
(8), but a positive Hilbert eigenstate or real-frequency flux statement
does not follow there. This is a scoped obstruction for this incoming
coefficient extraction; it excludes neither other geometric readouts nor
an enlarged system with an independently justified observability theorem.

The repository's [modular Hodge benchmark](../../../../susy-positivity/investigations/wilson-loewner/WZW/notes/MODULAR_HODGE_SCATTERING_AND_CUSP_COUPLING_TEST_20260923.md)
has a different fixed-half-shift ratio and a physical radiation slice. Its
successful Hodge completion does not remove (4), (7), or (8) for the heat
amplitude considered here.

## 4. Raw readouts, approximation, and next test

At fixed time, the exact cusp lift (6) supplies

\[
H_t^{(j)}(x)=\frac{i^j}{8\,2^j}
 e^{-qs/2}(\partial_s-q/2)^jV_t(s,q),\qquad0\le j\le4.
\tag{9}
\]

At time zero the completed coefficient can equivalently be differentiated
as `sum_{k=0}^{min(2,j)} binom(j,k)c^{(k)} Lambda_R^{(j-k)}`; discarding
the `c'` or `c''` terms is incorrect. Formula (9) uses one common physical
height and has no cutoff. To use the manuscript's finite arithmetic
readout, freeze its natural integer `N` at the center and retain
`|Q^{(j)}-F_N^{(j)}|<=j! L^j eta_N`. Any threshold jet test must also pay
the full measured quadratic error and normalizer term from Note 13.

A next construction must first supply a boundary pairing valid on the
spectral slice (8), or a different exact extraction that stays in a positive
spectral channel. It must intertwine the completed heat generator before
appealing to positivity. Computing another lossless cusp load at a fixed
frequency would not address these printed mismatches. This scout gives
exact zero-time extraction and three scoped obstructions, not a positive
collision exclusion or an RH conclusion.

The [exact checker](../numerics/check_automorphic_scout.py) verifies the
completion commutator, cusp-gauge coefficients, eigenvalue residual, and
physical spectral slice as rational polynomial identities. It does not
certify a Maass–Selberg estimate, continuum domains, or a heat-collision sign.
