# ADR-005: Release And Delivery Trust Chain

- Status: accepted
- Evidence cutoff: July 22, 2026

## Decision Statement

Product changes use GitHub pull requests and hosted checks; release-please prepares version changes, while a trusted maintainer creates a signed release tag and the downstream Cloudflare connection performs deployment outside the public Actions workflows.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Implementation | Check, dependency-review, and release-please workflows exist; release automation skips automatic GitHub release creation. | Workflow files; `RELEASE_WORKFLOW.md`; source ADRs 0001, 0011, 0015 | Repository rules and external deployment are not visible. |
| Runtime/live state | Selected cutoff-eligible hosted checks and releases succeeded/existed. | [GitHub packet](../../../evidence/packets/github-history-and-hosted-ci.md) | Success does not prove approval, deployment, or runtime health. |
| Rationale | Separate automated preparation from human release identity and maintain upgrade provenance. | Source ADRs 0001 and 0015 | Actual enforcement is unknown. |
| Approval | Source ADRs and release documentation describe the process as accepted. | `docs/adr/`; `RELEASE_WORKFLOW.md` | Signer recovery and successor authorization are unknown. |

## Constraints, Options, And Tradeoffs

Human signing reduces fully automated release compromise but adds a critical identity and availability dependency. The demo infrastructure and instance repositories have no public CI/release history, leaving their change-control path weakly evidenced.

## Impacts And Boundaries

A product successor may be able to build a fork but cannot publish trusted continuity releases without signer/rule authority. A third party can establish a new trust root, but that is not equivalent to inheriting the existing community identity.

## Change, Reversal, And Follow-Up

Close OI-002 by proving at least two recoverable release/admin paths and exercising a successor release in a safe repository. Preserve signed-tag verification during any transfer.
