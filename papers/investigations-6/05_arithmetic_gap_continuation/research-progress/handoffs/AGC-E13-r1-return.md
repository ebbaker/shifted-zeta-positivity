# AGC-E13 r1 return: centered log-disk allowance

19 November 2026, America/New_York. Prepared for **Edward Baker** with OpenAI
Codex LLM assistance. Helper explicitly dispatched **gpt-6.1-sol / ultra**;
independent backend/effort attestation was unavailable to the helper.

Status: **proved in-note**, one proof plus one author correction pass;
separate helper assessment required before acceptance. No canonical data,
source certificate, numerical campaign, coverage or cost claim.

Deliverable: [Note 08](../../notes/08_AGC_E13_LOG_DISK_ALLOWANCE_20261119.md).
Frozen inputs: [E13 r1](AGC-E13-r1-request.md),
[B02](../../brainstorm/notes/03_AGC_B02_LOG_DISK_REFINEMENT_20261119.md),
B01 physical reference/circle/equations and inherited E10/Section 7
endpoint formula. Only this return and Note 08 were written.

Proved for $|w|\le q<1$:

\[
\left|\log(1+w)-\kappa\right|\le\eta,\qquad
\kappa=\tfrac12\log(1-q^2),\quad\eta=\operatorname{atanh}q.
\]

Normalization to the disk centered at $\cosh\eta$ followed by the
Cayley map gives the proof. The radius $\eta$ is minimal for a containing
disk, by the two real endpoints. The disk need not equal the log image.

The common centered logarithm's two negative Fourier coefficients satisfy
$|a_1|^2+|a_2|^2\le\eta^2$, and the **complete** endpoint error is

\[
\Delta D=-r^2a_2+(c_P-X)ra_1-r^2a_1^2/4.
\]

With $d=|c_P-X|/r$, its exact abstract coefficient-ball allowance is

\[
B_{\rm joint}=r^2F(\eta,d),\qquad
F=\max_{0\le x\le\eta}
\left(\sqrt{\eta^2-x^2}+dx+x^2/4\right).
\]

This is an outer relaxation, not claimed sharp for the actual logarithm
image or physical theta data. Explicit bounds:

\[
F\le\eta\sqrt{1+d^2}+\eta^2/4,\qquad
F\le\eta+\frac{\eta d^2}{2-\eta}\quad(0<\eta<2).
\]

For $d=0$, $F=\eta$ if $0\le\eta\le2$, and
$F=1+\eta^2/4$ if $\eta\ge2$. At larger eta or nonzero offset the scalar
maximum and Cauchy bound remain valid; the parabolic bound is not used
at or above two.

For every $0<q<1$, $\eta<\lambda=-\log(1-q)$, so

\[
B_{\rm joint}
\le r^2(\eta\sqrt{1+d^2}+\eta^2/4)
<r^2(\lambda\sqrt{1+d^2}+\lambda^2/4)
\le r^2((1+d)\lambda+\lambda^2/4).
\]

Thus the refinement strictly beats **both** E10's stronger square-root
baseline and the earlier separate sum, at identical $q$, geometry and
reference/count/source payments. At $q=0$ they all vanish.

At $q=1/2$, $c_P=X$, the exact new allowance is
$\tfrac12r^2\log3$, versus
$r^2(\log2+(\log2)^2/4)$ for both baselines. A symbolic positive-series
argument proves the new allowance is less than $17/25$ of that baseline:
**more than 32 percent smaller**, with no floating computation.

The fixed contour has not been recentered, and its center need not equal
$c_P$ in the actual cell. Count two, contour clearance, analytic branch,
full source error, all-time and symmetry gates remain explicit. The
zero-error quadratic and Cluster 12 screen retain their collisions:
the strict reference-minus-complete-allowance margin fails at the event.

Exact full transport and direct endpoint evaluation remain the same
functional over the identical full admissible path set. The allowance
improvement is shared by both; it does not exclude temporal acquisition,
additional correlations, different costs or narrower feasible sets.

Next: separate assessment, then canonical acquisition of the actual
source/count/denominator/reference-gap and complete path inputs. No such
acquisition follows from this constant improvement.
