# Environment And Service Continuity View

Reader question: Which service and data dependencies must remain available or recoverable for library measurement and reporting?

## Evidence Boundary

This view uses approved source at commit `9cc669b97ece3ecd37fcb3950791cb3873d7944d` and cutoff-bounded public product material. It is not a library deployment inventory. No live topology, capacity, configuration, owner, backup, or vendor runtime was observed.

## Evidence Dimensions Used

Implementation and public responsibility statements are present. Observed operation, ownership/approval, cost, capacity, and recovery effectiveness are unknown.

## Current Source-Bounded Position

| Required outcome | Source-visible dependencies/mechanisms | Interruption effect | Live/option boundary | Evidence and closure |
|---|---|---|---|---|
| Receive visitor events | Browser tracker, Phoenix endpoint, event/session buffers, ClickHouse ingest repo | Measurement can stop or accepted events can remain only in process memory before flush. | Installed tracker versions, proxy, container count, buffer settings, and ClickHouse topology are unknown for Run; hosted implementation is not established by CE source. | [E-004](../../evidence/evidence-ledger.md#e-004), [E-035](../../evidence/evidence-ledger.md#e-035); [OI-001](../open-items.md#oi-001), [OI-002](../open-items.md#oi-002), [OI-003](../open-items.md#oi-003) |
| Authenticate staff and configure sites/goals | Phoenix, PostgreSQL, session/key material, mail for selected account flows | Dashboard/settings access and ownership transfer can fail even while collection continues. | Roles exist in source; account roster, 2FA, secret custody, mail, and successors are unknown. | [E-027](../../evidence/evidence-ledger.md#e-027), [E-034](../../evidence/evidence-ledger.md#e-034), [E-039](../../evidence/evidence-ledger.md#e-039); [OI-008](../open-items.md#oi-008), [OI-015](../open-items.md#oi-015) |
| Query dashboards/API/CSV | PostgreSQL configuration plus ClickHouse analytical queries | Reports can be unavailable although new events continue to arrive. | Readiness checks basic connectivity, not representative query correctness or seasonal responsiveness. | [E-003](../../evidence/evidence-ledger.md#e-003), [E-035](../../evidence/evidence-ledger.md#e-035); [OI-001](../open-items.md#oi-001), [OI-006](../open-items.md#oi-006) |
| Produce monthly email summaries | PostgreSQL-backed Oban, scheduler, ClickHouse queries, mail provider, recipients | The required monthly output may be delayed or missed independently of dashboards. | One-attempt delivery can complete after a caught mail error; live queue/mail/exporter evidence is absent. | [E-019](../../evidence/evidence-ledger.md#e-019), [E-036](../../evidence/evidence-ledger.md#e-036); [OI-006](../open-items.md#oi-006), [OI-014](../open-items.md#oi-014) |
| Delete or export data | PostgreSQL pending-deletion/job state, ClickHouse deletion/export queries, local or S3 output, notification mail | Exit, governance, and deletion can stall while the main dashboard remains usable. | CE source does not schedule the cleanup worker in its self-host cron set; external CE automation and hosted behavior are unknown. | [E-037](../../evidence/evidence-ledger.md#e-037), [E-039](../../evidence/evidence-ledger.md#e-039); [OI-008](../open-items.md#oi-008), [OI-015](../open-items.md#oi-015) |
| Upgrade and restart | Exact image, runtime configuration, both stores, interwoven migrations, optional session transfer | A partial migration, incompatible rollback, or abrupt loss can affect collection, reporting, or consistency. | Deployed tag/digest, release process, backup, and restore evidence are absent. | [E-038](../../evidence/evidence-ledger.md#e-038); [OI-004](../open-items.md#oi-004), [OI-005](../open-items.md#oi-005) |

## Material Unknowns And Closure Routes

Build the read-only Run inventory in [OI-001](../open-items.md#oi-001), set tolerances in [OI-002](../open-items.md#oi-002), exercise bounded non-production failure/recovery in [OI-003](../open-items.md#oi-003)/[OI-004](../open-items.md#oi-004), and assign service/account successors in [OI-015](../open-items.md#oi-015). Do not infer Replace dependencies because no candidate evidence was approved.
