# Initial research program for angular jacobi gluing

13 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6.1-sol (`gpt-6.1-sol`), Codex; reasoning effort ultra, verified
from the recorded session configuration. Status: initialized, awaiting
Claude review. This is a proposed research program with established seeds;
no new signed estimate, numerical run, or RH claim is recorded here.

## Source evolution and physical observation

Retain the full integer theta field
\[
\Theta(r,y)=\sum_{n\in\mathbb Z}e^{-\pi n^2r+2\pi iny},\qquad
k(u,y)=e^u[\Theta(e^{4u},y)-1],\quad u\ge0.
\]
The prepared field is \(e^{tu^2}k(u,y)\), with Newman generator
multiplication by \(u^2\). Its half-line transform
\(\mathcal T_t(z,y)=\int_0^\infty e^{tu^2+izu}k(u,y)\,du\)
is entire on bounded complex parameter sets by the theta tail. At
\(y=0\), \((\partial_u^2-1)k/16=\Phi\) supplies the genuine source.
The physical observation is \((H,H_x)\), obtained through this insertion
and its endpoint terms, rather than directly selecting \(\mathcal T\).

With \(J=\Re\mathcal T_t(x,0)\), the exact reduction is
\[
16H=1+(2t-1-x^2)J+4txJ_x-4t^2J_{xx}.
\]
The constant comes from the zero-mode-subtracted endpoint. Differentiating
this equation gives the physical slope with every coefficient derivative.

## Objective and established seed

The full Jacobi partner, integer coefficients, and angular derivatives may
constrain a complete signed source quantity more strongly than the scalar
endpoint hierarchy. The existing angular identity is
\[
\mathcal T_{yy}(z-4i,y)/\pi
=-k(0,y)+2it\mathcal T_z(z,y)-(1+iz)\mathcal T(z,y).
\]
The objective is an additional source-selected relation yielding visibility
of \((H,H_x)\), or one of the complete stationary signs. An angular norm
or a second derivation of the displayed equation is useful bookkeeping,
but does not yet meet that objective.

## First bounded task

Choose one Jacobi modular generator and a bounded parameter rectangle.
Transform the prepared field, zero mode, half-line domain, and physical
insertion together. Write its generator, preparation, projection, and
boundary defects separately. Identify a combination of angular derivatives,
endpoint data, and shifted spectral channels that reduces to the actual
pair or a complete stationary product. Derive a majorant for the entire
\(z-4i\) channel before approximating it. The first deliverable should be
one exact identity, its domain and complete error ledger, and a precise
statement of the remaining signed inequality.

## Validation and decision criteria

Check the transformed identity first against the direct full-source
formula, including all endpoint constants. A finite algebra check can
diagnose signs and insertions; an asserted numerical margin needs outward
bounds and infinite-tail payment. Apply candidate equations only to the
complete physical readout. Continue if full gluing adds a nonredundant
relation or reduces a stated residual after all costs. Record a bounded
negative result if the calculation reproduces the affine hierarchy without
new information, or if shift growth consumes the proposed gain.

Jacobi heat in \((r,y)\) differs from Newman multiplication by
\((\log r)^2/16\). Their compatibility must be calculated. The genuine
Fourier coefficients are all one; the angular PDE alone permits other
preparations. Zero subtraction, modular factors, complex angular arguments,
normalizer derivatives, and cutoff transitions remain explicit. The
existing small approximation disk does not cover a fixed shift by \(-4i\).

## Starting records

- [Brainstorm card 2](../../../inactive/brainstorm/LIFTED_THETA_SYMMETRY_SEARCH_CODEX_20261013.md#2-angular-jacobi-gluing-and-heat-compatible-shifts).
- [Exact angular field, Heat Note 25 §6](../../../../quasi-rh-exponent-descent/newman_collisions/notes/25_ENLARGED_STATE_TRANSPORT_CHORD_DYNAMICS_AND_THETA_GLUING_20261010.md).
- [Rotor insertion and endpoint hierarchy](../../../../quasi-rh-exponent-descent/newman_collisions/06_theta_lattice/notes/1_ROTOR_ZERO_MODE_WARD_IDENTITY_AND_SECTOR_MISMATCH_20261010.md).
- [Jacobi transformation, DLMF 20.7.32](https://dlmf.nist.gov/20.7.E32).
