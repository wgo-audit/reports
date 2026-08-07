# ADR-009: Container Runtime Boundary

- Status: observed
- Evidence cutoff: 2026-08-06

## Decision Statement

The repository ships a multi-stage Alpine/Ruby container with application code under `/app`, state under `/data/docuseal`, native PDF/image/ML dependencies, Puma on port 3000, and a Compose example combining DocuSeal, PostgreSQL and Caddy with mutable tags. The image creates UID 2000 but lacks a `USER` directive; startup can continue as the original identity if privilege reduction fails.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Implementation | Container build/runtime and Compose ingress/state example | [Runtime packet §1–3](../../../evidence/packets/architecture-runtime-deployment-delivery-identity-secrets.md) | Example is not a hardened production baseline |
| Runtime/live state | unknown | No orchestration, network, digest or identity evidence | Effective isolation/health unknown |
| Rationale | unknown | No deployment ADR found | Example convenience is not target design |
| Approval | unknown | No IT Operations/CISO approval | Hardening and support unapproved |

## Constraints, Options, And Tradeoffs

Container packaging improves reproducibility but does not choose ingress/TLS, network segmentation, immutable images, readiness/liveness, writable paths, storage backup or process separation. Target orchestration can harden these without modifying product code.

## Impacts And Boundaries

Native PDF/image dependencies and writable state are part of the security/recovery boundary. See the [deployment/runtime diagram](../diagrams/deployment-and-runtime-path.md).

## Change, Reversal, And Follow-Up

OI-003 defines the target runtime; OI-004 must create the hardened deployment and upgrade baseline. Do not treat the Compose file as approved production architecture.

