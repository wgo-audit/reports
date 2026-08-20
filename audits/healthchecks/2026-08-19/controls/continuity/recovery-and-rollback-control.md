# Recovery And Rollback Control

## Evidence Boundary

This view defines evidence required for recovery approval; it is not a runbook
and does not authorize deployment. Source evidence is
[E-008](../../evidence/evidence-ledger.md#E-008) and
[E-028](../../evidence/evidence-ledger.md#E-028). No Acme backup, restore,
rollback, drill, data store, owner, or recovery objective was provided.

## State And Recovery Boundaries

| State or dependency | Source-observed behavior | Required recovery proof | Current result |
|---|---|---|---|
| Relational database | Authoritative checks, pings, flips, notification state, users, projects, and channel values; startup can apply data-changing migrations. | Versioned backup before change, integrity check, isolated restore, application compatibility, and measured recovery. | Unknown; OI-007 |
| Optional object store | Bodies over 100 bytes can be externalized; upload occurs after relational save; disabling S3 loses access to those bodies and no reverse-migration tool is documented. | Restore/reconcile database and objects to a consistent point; test missing/partial objects; preserve data lifecycle. | Unknown; OI-007 |
| Application image/config | Published version tags are available; the reference container applies migrations before serving. | Immutable image/digest and config/secret version, deploy precheck, rollback decision point, and evidence that old code can safely use restored schema/data. | Unknown; OI-007 and OI-008 |
| Alert backlog | Unprocessed flips are durable, but a flip is claimed before delivery completes. | Exercise worker death before/after claim, database interruption, provider failure, restart, and compensating detection without duplicate or lost critical notice. | Not proved; OI-006 |
| Monitor definitions and routes | Management API exposes checks and limited integration identity; project ownership can transfer. | Acme-controlled inventory/export, secret-safe recreation, destination verification, producer URL cutover, and rollback. | Unknown; OI-009, OI-011, OI-012 |

## Approval Sequence

For **pull**, prove database and any object-store restore, immutable rollback,
alert-worker restart, and independent notification before production. For
**make**, repeat the same evidence after every upstream merge and fork release.
For **buy**, obtain vendor recovery/continuity evidence and prove Acme's
account/exit copy, alternate route, and producer cutover; public status is not
restore evidence.

Recovery targets are unresolved. [OI-013](../open-items.md#OI-013) asks the CTO
to set maximum monitoring-service recovery time and acceptable loss of monitor
configuration/event history. Until then, the five-minute human-alert contract
still requires an independent parallel path during service recovery.
