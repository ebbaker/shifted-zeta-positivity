# Circle heat and full Jacobi normalization check

27 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**.

Source: **National Institute of Standards and Technology, NIST Digital Library of Mathematical Functions**, Chapter 20. Online passages retrieved 27 October 2026. This extends the existing DLMF catalog entry; it does not create a second source identity or a whole-chapter audit.

| Checked passage | Use in the current calculation |
| --- | --- |
| [20.2.3](https://dlmf.nist.gov/20.2.E3) | K(s,theta)=theta_3(pi theta given i s), including both positive and negative integer modes |
| [20.13.1–2](https://dlmf.nist.gov/20.13) | Rescaling the elliptic argument gives K_s=K_theta_theta/(4 pi); this parameter is distinct from physical heat time |
| [20.7.32](https://dlmf.nist.gov/20.7.E32) | Principal-root transformation at s>0, with the full elliptic argument retained: K(s,theta)=s^(−1/2) exp(−pi theta²/s) K(1/s,i theta/s) |

The series also directly verifies the heat factor. The full modular formula sends a real auxiliary argument to an imaginary argument. Only the zero-argument restriction directly supplies the scalar reflection used here.

[Note03](../notes/03_CIRCLE_HEAT_LIFT_AND_BOUNDARY_TRANSFER_OBSTRUCTION_20261027.md) derives the radial differential combination, commutators, tail conditions and boundary obstruction separately. Those deductions are not attributed to DLMF. No further theorem or literature-priority conclusion is imported. This is an online reference; no artificial PDF or new book download was made. The existing Axler PDF and its provenance remain unchanged.
