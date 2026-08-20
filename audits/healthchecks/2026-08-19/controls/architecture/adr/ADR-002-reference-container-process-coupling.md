# ADR-002: Reference Container Couples Web And Background Processes

- Status: observed
- Evidence cutoff: 2026-08-19

## Decision Statement

The supplied Docker deployment starts a single web service that runs database
migrations before serving and attaches `sendalerts`, `sendreports`, and optional
SMTP daemons to the uWSGI master. The sample Compose file places that service and
a single PostgreSQL node on one host.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Implementation | One Compose `web` service depends on one `db`; uWSGI runs migrations and attaches background daemons. | [E-004](../../../evidence/evidence-ledger.md#E-004), [deployment diagram](../diagrams/deployment-and-runtime-path.md) | It is a sample/reference configuration, not a production claim. |
| Runtime/live state | unknown | [OI-005](../../open-items.md#OI-005) | No Acme host, orchestrator, database, network, or process state was approved. |
| Rationale | Upstream documentation explicitly says the sample chooses a single-host topology for simplicity. | `HC-CODE-001:docker/README.md:1-8` | No evidence that simplicity is acceptable for Acme's critical-monitoring use. |
| Approval | unknown | [audit brief](../../../audit-brief.md) | Acme has not selected pull, make, or buy. |

## Constraints, Options, And Tradeoffs

- The image is convenient and keeps upgrade commands aligned with releases, but
  a web-container or uWSGI-master failure also removes the attached alert worker.
- Startup migrations reduce operator steps but couple schema changes to service
  start; migration history includes transformations and deletion, so safe
  rollback requires external backup and release discipline.
- The sample has no TLS terminator, load balancer, replica, independent process
  monitor, backup resource, or restore/rollback workflow.
- Operators can run processes separately and use managed infrastructure without
  forking application code; those changes remain a pull scenario if they do not
  create a product fork.

## Impacts And Boundaries

The sample Compose file must not be treated as the target architecture for an
operationally critical service. Pull is an application-source choice, not an
authorization to use the sample topology unchanged. A production self-hosted
design can separate failure domains without entering make.

## Change, Reversal, And Follow-Up

Close [OI-005](../../open-items.md#OI-005) with an approved topology and
[OI-007](../../open-items.md#OI-007) with tested release/recovery controls. Keep
image versions immutable; rehearse restore and rollback before allowing startup
migrations against production data. A fork is not justified by these deployment
gaps alone.
