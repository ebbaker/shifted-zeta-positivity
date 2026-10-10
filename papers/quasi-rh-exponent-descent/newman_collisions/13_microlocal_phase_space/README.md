# Microlocal phase space and coherent observations

10 October 2026. Model: GPT-6 (Codex); exact serving variant and configured reasoning effort unavailable and not inferred. Checks are internal, not independent mathematical review.

This folder implements program 13 in [Heat Note 14](../notes/14_DIMENSIONAL_REDUCTION_AND_SUPERSYMMETRIC_HEAT_PROGRAM_20261010.md), beside the existing `01_analytic_gaussian` project.

The exact positive Husimi lift retains a generator with negative momentum diffusion, a spatial cross derivative, and a contact term. Its genuine scalar readout requires Gaussian reconstruction and derivative drift. The doubled arithmetic density matrix keeps both phase differences and reflected phase sums; removing those entries reproduces the failed diagonal packet comparison.

[Initial result](notes/1_HUSIMI_READOUT_DRIFT_AND_COHERENT_INTERFERENCE_20261010.md) gives the genuine state, reduction map, domains, backward-heat sign, derivative and normalizer dictionary, and the remaining obstruction. [Internal review](reviews/1_SCOUT_INTERNAL_REVIEW_20261010.md) records scope and checks; [numerics](numerics/README.md) supplies a small reproducible replay.

Next bounded task: Seek an interference-sensitive inequality for a composite-complete genuine block, recombined with a measured full-sum remainder smaller than the collision or threshold-jet margin.

[Note 2](notes/2_CENTERED_RELATIVE_BLOCK_AND_ADVERSE_COHERENT_CURRENT_20261010.md)
now supplies an exact centered-moment transformation of the genuine relative
block `N/2 < n <= N`, its full complement interference, and a paid necessary
coherent-current condition at genuine collisions. A standard-library outward
interval certificate gives a **negative block current** at the actual
shrinking-sector height `x = 4*pi*22066^2`, with `t = 1/(2*log(22066))`.
This is a macroscopic-block sign obstruction, not a complete-state sign or an
actual collision. [Review 2](reviews/2_CENTERED_BLOCK_AND_CURRENT_INTERNAL_REVIEW_20261010.md)
records the checks. The next signed checkpoint is the complete candidate
current, including its complement and cross terms, or the complete paid
fourth-jet expression assembled from the centered moments.

[Note 3](notes/3_COMPLETE_CURRENT_AND_PAID_SIMPLE_ZERO_RECTANGLE_20261010.md)
restores the complete genuine cutoff at `M=22066`, measures its complement
and both cross-phase channels, and certifies the full-current candidate
margin. It also proves **one unique simple genuine heat zero for every
time** in `t0 <= t <= t0 + 8e-6`, inside
`x0 + 0.3 <= x <= x0 + 0.4`, where `t0=1/(2*log(22066))` and
`x0=4*pi*22066^2`. The full paid normalized derivative `Q_t'` is greater than `10.20`
on this rectangle, so `H_t` and `H_t'` never vanish jointly there.
[Review 3](reviews/3_COMPLETE_CURRENT_RECTANGLE_INTERNAL_REVIEW_20261010.md)
records the finite scope, interval replay and internal cross-checks.

This certificate proves local joint nonvanishing on the stated rectangle.
No sectorwide collision exclusion, uniform current sign or RH conclusion
is claimed. Follow [LARGE_FILES.md](../../../../LARGE_FILES.md); the present
sources and small check records need no external archive.
