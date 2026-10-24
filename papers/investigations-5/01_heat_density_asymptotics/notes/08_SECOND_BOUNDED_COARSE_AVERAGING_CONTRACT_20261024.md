# Second bounded contract: coarse mass and weak transport

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**.

**Scope fixed after source-moment scouting, before the full comparison.**
This advances HDA-02/04 and tests a weak-current counterpart of HDA-06.
It is a finite approximation milestone, not an RH criterion. The existing
17-case local pilot is not rerun. This contract does not authorize claiming
a solved boundary problem or independent verification.

## Target and scales

Use the unchanged H and rho of [Note 02](02_FILTERED_EVOLUTION_AND_FLUCTUATION_IDENTITIES_20261024.md).
Fix epsilon=1e-4 in the original amplitude units. The auxiliary normalized
source integral f=H/M, M=H(t,0)>0, is only an evaluation device: its
regulator is eta=epsilon/M, not a newly chosen fixed relative regulator.
The target density is unnormalized.

Use the same k(q)=315(1-q^2)^4/256 on [-1,1] as round one, with **fixed**
spatial halfwidths lx=10 and hy=3/4. The observation box is
x in [-2,2], y in [-1/2,1/2], t in [512,1024]. The spatial buffer is
[-12,12] x [-1.25,1.25]. Evaluate the finite sample x=0,1,2,
y=0,1/4,1/2 at t=512,768,1024. Symmetries do not add independent samples.
The width 20 contains approximately seven to nine carrier density periods.
No sampled result constitutes coverage of the continuous time range.

Also evaluate a centered offline time average at t=768, halfwidth tau=64,
using k in time. All filters are fixed. Auxiliary contours may move with
time without moving the target filter; differentiations concern the fixed
kernel. No moving-filter commutator is suppressed.

## Source transfer and regulator separation

Let mu=E_t u, v=Var_t u. Compare f to
A(z) cos(mu z), A(z)=1-v z^2/2. A third absolute centered moment with an
exponential transverse weight bounds the remainder. Check a finite
complex rectangle with x walls X=6 pi/mu and y walls +/-1.25; it must
contain the spatial support and the carrier disks. Check A nonvanishing,
disjoint disks and a strict carrier margin before interpreting contours
as observations of real zero mass. These are conditional analytic
implications; finite source quadratures do not certify their premises.

Use the disks to supply the lower bounds in Note 06, without fitting
individual theta zeros. Evaluate the resulting regulator-bias bound in
logarithmic units. Very small eta must not underflow to a claimed zero
error. Keep source quadrature uncertainty distinct from regulator bias.

## Weak observables and the proposed mean

The proposed leading density is Rm=(mu/pi) k_h(y). Its zero-measure
current model is Jm=-(mu'/pi) x k_h(y), with
mu'=2 mu v+E_t[(u-mu)^3]. Its continuity equation is exact algebraically;
accuracy is tested against source contours, not inferred from that identity.

For each x center c, use the analytic polynomial
P_c(z)=(315/(256 lx))(1-((z-c)/lx)^2)^4 on the rectangle
[c-lx,c+lx] x [-.75,.75]. Conditional on real simple zeros and nonzero
boundary values, residues give the weighted zero mass, real transport,
and time derivative from P H_z/H, P H_zz/H, and P' H_zz/H, respectively.
Multiplying by k_h(y) gives the reported spatial observables. There is
no theta root finding or peak-density quadrature. A contour count checks
the outer rectangle. Record the finite-lattice cosine value separately
from the phase-homogenized mu/pi model.

Measure density relative error, current relative error for c != 0, and
time-derivative relative error. At c=0 use absolute current error.
The differentiated diagnostic is the weak current discrepancy, not a
measurement of the full differentiated Q. Report the fixed-frequency
stationary baseline as zero time derivative/current. Regulator removal
for the current is a limit statement; no finite-epsilon current-error
bound is to be inferred from a density-bias bound.

## Numerical checks and decision rule

Use composite source quadrature with panels of width .125, orders 32/48,
cutoffs 3/3.25 and 8/12 theta summands. Evaluate in scaled exponentials.
Use 96/160 nodes per contour edge, a displaced contour of height 1 with
192 nodes, time differences .5/.25 with Richardson extrapolation, and
12/20-node temporal filtering. Changes below 1e-8 for mass and 1e-9 for
current/derivative are the initial diagnostic targets. Refine failures;
preserve the failed comparison. They are not interval error bounds.

An exploratory useful outcome is below 1% mass error and below 10%
current/derivative error in the stated finite samples, with the analytic
transfer and regulator formulas explicitly evaluated. A failed target
remains evidence about this approximation and scale, not a universal
obstruction. Broad covariance accuracy and evolved-solution stability
remain separate gates even if these observations succeed.

Check the contour formulas on a fixed-frequency cosine with an exact
finite-lattice sum. Check the source-concentration gate on the double
event of H=(1+exp(4(t-1/4))cos(2z))/2. Apply the existing four-family
[collision screen](../../../../result-summaries/12_collision_controls_and_screening.md)
at the premise level; do not rerun old certificates.

Keep one [progress ledger](../research-progress/01_AVERAGED_DENSITY_RESEARCH_PROGRESS_20261024.md),
save code and its small record in numerics, and record a same-assistant
assessment. The [result index](../../../../result-summaries/README.md)
and [avoid index](../../../../avoid/README.md), especially
[classification](../../../../avoid/01_restating_the_target.md) and
[status discipline](../../../../avoid/06_status_stronger_than_the_evidence.md), apply.
