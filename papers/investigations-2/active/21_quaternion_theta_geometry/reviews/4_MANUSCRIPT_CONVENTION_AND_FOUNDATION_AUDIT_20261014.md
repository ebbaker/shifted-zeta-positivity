# Manuscript convention and foundation audit

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6.1-sol (Codex)**; reasoning effort: **ultra**.


Scope: the [standalone manuscript](../manuscript/quaternion_theta_geometry.tex).
Three LLM tasks separately derived the RH foundation, quaternion equations,
and theta estimates. The integrating agent checked each derivation, and
the theta task independently reread the RH and quaternion sections. This
is internal verification, not specialist refereeing or formal proof.

## RH foundation and exact logical dependencies

The Jacobi/Mellin calculation establishes the complete even theta source,
the boundary value A'(0)=-1/2, and H(0,z)=xi(1/2+iz/2)/8, with both
integrations by parts displayed. Complete-source decay establishes joint
entireness, the backward heat sign, fixed-time order at most one, and
nonvanishing on the imaginary axis.

The manuscript explicitly states the deep global inputs rather than
assigning them to Fueter regularity: classical strip contraction, the
Newman threshold, and uniform positive-time zero localization. The
localization and strip statements were checked against Polymath's
arXiv:1904.12438v2, Theorem 1.5(i) and Theorem 3.2. The threshold endpoint
and compactness proof include the hypotheses preventing zeros from
escaping to infinity. Rodgers--Tao is contextual, not required for this
collision equivalence.

Hermite splitting is derived with the probabilists' normalization and
sqrt(2(t-T)) scale. The even-multiplicity stationary chart is proved by
analytic rescaling. Applying it to H or H_x covers both multiplicity
parities, and both bounded-loss ratios diverge as r/(T-t)+O(1) on the
appropriate predecessor. Necessity follows from paired Hadamard products
and real-rooted polynomial approximations. Thus the global stationary
sign and bounded-loss formulations are equivalences for the genuine theta
family, with limited-domain statements retaining their actual coverage.

The vertical scalar curvature, monotonicity and logarithmic-derivative
criteria are proved in the even order-at-most-one class. The manuscript
does not replace scalar curvature by the quaternion norm curvature.

## Quaternion conventions and translations

The proof starts with Hamilton multiplication and complex coefficients on
the right of j. It derives q=z0+jz1=a+ib+jc-kd, including the sign on the
fourth real coordinate, and the normalized standard left Fueter operator.
Complex coordinate derivatives of quaternion fields are explicitly
componentwise; they are not a different left-i Wirtinger operator.

The adopted lift uses tau=t+bar(z1), with external time independent.
The jet constraint, regularity, conjugate-Fueter heat equation, and
translation F(t,q)=F(0,q+jt) are derived. The physical real trace is the
common scalar first jet, so the compact RH criterion is a direct
translation of the separately proved scalar collision theorem.

The j coefficient of conjugate(G_l)G_(l+1) is minus the complex Laguerre
form; both j and k orientations were checked at complex points. The
stationary union and scalar curvature use the declared complex projection.
The real Jacobian equals minus the squared modulus of the complex
Laguerre determinant, because output coordinates reverse Im(H_z).
The real Jacobian at a double collision is nonzero and does not exclude it.

The Cauchy and Borel--Pompeiu formulas were rederived from ordered Stokes
with kernel-normal-field multiplication, unit sphere flux, and residual
factor -2 for the half-normalized operator. The spherical constants 4
and 6 follow by differentiating the four-dimensional harmonic Poisson
kernel. Currents, norm and logarithmic-norm formulas, reciprocal failure,
and polynomial controls retain their exact signs and domains. The primary
quaternion source is Frenkel--Libine, Theorem 9 and Theorem 34, with the
real-coordinate conversion done in the manuscript itself.

## Theta estimates and remaining scope

The complete-source core, entire tail, signed moment remainder, and
central norm bound were checked without theta truncation or quadrature.
The angular defect retains every Fourier coefficient at the declared
single scale. Its half-line observation class and modular smoothness
limitations are explicit. The remote perturbation construction uses a
nonzero coefficient change and verifies failure of smooth reflection.

The paired kernel includes all arithmetic cross terms. Individual
channels have the displayed negative algebraic Laguerre tails. The
manuscript additionally spells out a positive-polynomial derivative
majorant for endpoint-compensated truncation, including the complete
geometric index tail and the threshold pi(N+1)^2 >= 8K+9. Its coefficient
recurrence, degree bounds, integration decay, and successive ratio bound
were checked analytically. A finite compensation order still gives an
absolute algebraic remainder, not a global relative theta estimate.

## Replays and document validation

- [Coordinate algebra checker](../numerics/check_quaternion_coordinate_algebra.py)
  and [record](../numerics/QUATERNION_COORDINATE_ALGEBRA_CHECKS_20261014.json):
  58 exact rational checks pass, including complex lift values, Hamilton
  products, Fueter and heat equations, signed components, and the real
  Jacobian orientation.
- [Boundary checker](../numerics/check_fueter_boundary_identities.py) and
  [record](../numerics/FUETER_BOUNDARY_IDENTITY_CHECKS_20261014.json):
  all 14 polynomial cases, sphere moment checks, and controls pass.
- [Central checker](../numerics/check_theta_central_moment_bound.py) and
  [record](../numerics/THETA_CENTRAL_MOMENT_BOUND_20261014.json): 17 checks pass.
- [Gluing checker](../numerics/check_theta_gluing_defect_constants.py) and
  [record](../numerics/THETA_GLUING_DEFECT_CHECKS_20261014.json): 22 checks pass.

The [build record](../manuscript/BUILD_RECORD.json) records source and PDF
hashes. The standalone source compiles with the desktop editor's compiler;
the exported PDF has 26 pages. Internal references and bibliography resolve,
all 113 labels are unique, and the export log has no layout or unresolved
reference warnings. Every page was visually inspected in contact sheets,
with full-page inspections of the coordinate, kernel, and final pages.
All research files remain below 1 MiB. No manuscript snapshot, commit,
or global RH sign claim was created by this integration.
