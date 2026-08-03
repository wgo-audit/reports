# ADR-007: Git-Backed Instance Data And Recovery Boundary

- Status: observed
- Evidence cutoff: July 22, 2026

## Decision Statement

Human-authored instance configuration and link history are durable in Git; runtime files are disposable derived artifacts, while provider state, credentials, and account recovery remain external.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Implementation | `custom/v8s-links.txt`, configuration JSON, and Wrangler configuration feed the build; generated runtime is read-only. | `docs/README.md`; build/runtime source; website security model | Clean rebuild and restore were not run. |
| Runtime/live state | Rollback guidance points to Git/Cloudflare last-known-good deployments. | `RELEASE_WORKFLOW.md`; [recovery packet](../../../evidence/packets/recovery-and-operations.md) | No rollback or restore exercise was observed. |
| Rationale | Reviewable configuration history and disposable deployment reduce mutable-state complexity. | Product docs and source ADRs | External control-plane state remains a recovery dependency. |
| Approval | Source and documentation consistently use Git as instance authority. | [E-004/E-007](../../../evidence/evidence-ledger.md) | No successor acceptance or recovery objective is recorded. |

## Constraints, Options, And Tradeoffs

The core link dataset is portable, but the current public service identity is not: domain, DNS, Cloudflare account, Terraform state, deployment connection, secrets, and monitoring must also be recovered or replaced.

## Impacts And Boundaries

A third party can recreate functionality on a new domain/account from public source. It cannot be presumed able to preserve the existing domain, trust, release lineage, or live controls.

## Change, Reversal, And Follow-Up

Define recovery objectives and test restoration into an independently controlled account. Record only redacted inventories and proof, never secret values.
