# Recovery And Control View

Reader question: What recovery mechanisms are visible, and what proof is still required before calling Run or Subscribe dependable?

## Evidence Boundary

The view uses approved code/configuration, the [recovery packet](../../evidence/packets/recovery-and-operations.md), and bounded public hosted statements. No restore, failover, rollback, incident, alert, live traffic, or production state was inspected or exercised.

## Evidence Dimensions Used

Implementation and public declarations are present. Observed recovery, approved RPO/RTO, accountable ownership, and hosted contractual/control evidence are unknown.

## Current Source-Bounded Position

| Interruption | Detection visible in source/public material | Source-visible recovery/control | Missing acceptance proof | Route |
|---|---|---|---|---|
| PostgreSQL unavailable | Readiness `SELECT 1`; logs/conditional telemetry | Process supervision and database reconnect behavior from dependencies; no repository-owned restore | Backup scope, replication, corruption detection, RPO/RTO, dated restore | [OI-004](../open-items.md#oi-004) |
| ClickHouse unavailable/corrupt | Readiness `SELECT 1`; query/ingest exceptions; conditional metrics | Buffered write attempt, multiple repo roles; no repository-owned restore | Accepted-versus-stored reconciliation, analytical consistency, backup/restore, peak tolerance | [OI-002](../open-items.md#oi-002), [OI-003](../open-items.md#oi-003), [OI-004](../open-items.md#oi-004) |
| Application orderly restart | Liveness/readiness endpoints | Termination flush; optional session-cache transfer with 15-second shutdown delay | Successful transfer, correct orchestration/drain, loss measurement | [OI-003](../open-items.md#oi-003) |
| Application/host abrupt loss | External detection unknown | No durable in-repository queue before the embedded ClickHouse buffer write | Maximum event loss and session impact under representative configuration | [OI-002](../open-items.md#oi-002), [OI-003](../open-items.md#oi-003) |
| Background-job worker loss | Oban exception telemetry; PromEx definitions | PostgreSQL job state; Lifeline rescue after 120 minutes; configured queues/cron | Enabled state, backlog/failed-job alerts, 120-minute suitability, owner response | [OI-001](../open-items.md#oi-001), [OI-014](../open-items.md#oi-014) |
| Monthly mail-provider failure | Application log only on caught exception | None shown in the report job after the error tuple; one allowed attempt | Retry/alert/reconciliation or approved API/CSV alternative | [OI-014](../open-items.md#oi-014) |
| Upgrade/migration failure | Pending-migration command and command output | Interwoven up-migration; independent per-repo rollback command | Backup prerequisite, irreversible/non-atomic stop conditions, exercised cross-store restore | [OI-004](../open-items.md#oi-004), [OI-005](../open-items.md#oi-005) |
| Hosted-service outage/data loss | Post-cutoff page claims on-call monitoring, daily backup, quarterly restore | Vendor-controlled; internal mechanisms not approved | Negotiated availability/support, recovery objectives, evidence of restore/control operation | [OI-015](../open-items.md#oi-015) |

Evidence: [E-035](../../evidence/evidence-ledger.md#e-035)–[E-039](../../evidence/evidence-ledger.md#e-039), with hosted control claims bounded by [E-030](../../evidence/evidence-ledger.md#e-030).

## Material Unknowns And Closure Routes

No source mechanism or command proves recovery. Run requires coordinated PostgreSQL/ClickHouse and persistent-file backup plus non-production restoration and restart exercises. Subscribe requires procurement/assurance evidence rather than transfer of CE assumptions. Replace remains unknown without a candidate.
