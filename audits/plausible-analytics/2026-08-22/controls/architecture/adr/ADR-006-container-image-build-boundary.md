# ADR-006: Container Image Build Boundary

- Status: observed
- Evidence cutoff: 2026-08-22 22:08:28 EDT

## Decision Statement

`[Verified fact]` GitHub Actions builds and pushes cloud/EE images from `master`/`stable`/release tags and CE multi-architecture images from version tags; the repository-visible boundary stops before cloud promotion/deployment. [E-007](../../../evidence/evidence-ledger.md#e-007)

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Implementation | `[Verified fact]` Multi-stage pinned-base Dockerfile; separate private/public build workflows; pinned third-party Actions; marker/notification after private build. | [E-007](../../../evidence/evidence-ledger.md#e-007), [E-012](../../../evidence/evidence-ledger.md#e-012) | Build is not deploy. |
| Runtime/live state | `[Unknown]` Promotion, live image digest, migration, health gate, rollback, and approvers. | [OI-003](../../open-items.md#oi-003) | Branch protection endpoint required unavailable authentication. |
| Rationale | `[Reasoned inference]` Separate artifact channels support cloud cadence and CE releases. | E-007, E-011 | No architecture approval record. |
| Approval | `[Unknown]` | [OI-003](../../open-items.md#oi-003) | No promotion authority evidence. |

## Constraints, Options, And Tradeoffs

`[Verified fact]` The private image workflow is independent of the CI workflow. At the pinned commit the merge-group CI/check gate succeeded; the subsequent master image build succeeded while a separate push CI static job failed at dependency retrieval. `[Reasoned inference]` This makes the unknown promotion gate materially important; it does not prove an unsafe deployment.

## Impacts And Boundaries

`[Verified fact]` The image contains the OTP release and assets. `[Unknown]` Deployment configuration, infrastructure, secrets, migration invocation, rollback, and live Checkly/telemetry operation are outside repository-visible proof.

## Change, Reversal, And Follow-Up

Reconstruct commit-to-live provenance and test rollback/migration stop conditions through [OI-003](../../open-items.md#oi-003).
