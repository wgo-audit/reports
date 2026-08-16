# ADR-011: Release Image Provenance And Promotion

- Status: observed
- Evidence cutoff: 2026-08-06

## Decision Statement

Dotted Git tags trigger a multi-architecture Docker build/push, and the pinned tag's CI and image build completed successfully. The inspected workflow publishes tag-derived images but does not visibly create an SBOM, signature, attestation, vulnerability gate or deployment promotion record; public update guidance pulls an unqualified image.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Implementation | CI checks and tag-triggered AMD64/ARM64 image publication | [Runtime packet §16, §18](../../../evidence/packets/architecture-runtime-deployment-delivery-identity-secrets.md); [shared packet](../../../evidence/packets/github-history-and-hosted-ci.md) | Docker digest/assets and protected settings were not inspected |
| Runtime/live state | unknown | No registry digest or deployment record | Built image is not proven deployed image |
| Rationale | unknown | Internal `wip` review context unavailable | Merge/tag is not approval |
| Approval | unknown | No organization promotion authority | Workflow success is not release acceptance |

## Constraints, Options, And Tradeoffs

Upstream images accelerate evaluation, but a regulated target needs immutable digest intake, SBOM/vulnerability review, provenance verification, retention, environment promotion and rollback evidence. Organization-owned rebuilds add maintenance burden and must preserve AGPL/license/vendor considerations.

## Impacts And Boundaries

Pinned source alone does not make the deployed artifact reproducible. Mutable Actions and unverified Dockerfile downloads broaden supply-chain trust.

## Change, Reversal, And Follow-Up

OI-004 must establish artifact intake/promotion, digest pinning, verification, migration compatibility, canary/rollback and evidence capture before a production release.
