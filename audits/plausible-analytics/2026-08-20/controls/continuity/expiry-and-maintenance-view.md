# Expiry And Maintenance Continuity View

Reader question: Which time-bound controls or maintenance obligations can silently expire, stall, or invalidate continuity assumptions?

## Evidence Boundary

Approved source/configuration and public option statements were reviewed. No library maintenance calendar, certificate/account inventory, backup retention record, patch history, contract-renewal record, or hosted internal schedule was available.

## Evidence Dimensions Used

Implementation schedules and public release/support terms are present. Effective execution, ownership, approval, cost, and timeliness are unknown.

## Current Source-Bounded Position

| Time-bound surface | Source/public schedule or condition | Continuity risk | Required control |
|---|---|---|---|
| CE security maintenance | Security fixes target only the latest major.minor; CE is publicly described as a twice-yearly long-term release with community support. | An unidentified or delayed deployment can fall outside supported fixes; community response is not guaranteed. | Map exact digest/tag to release evidence and approve patch cadence/owner through [OI-005](../open-items.md#oi-005)/[OI-015](../open-items.md#oi-015). |
| Database migration/rollback | Migration is an explicit command; normal image startup does not run it. Some migration history is irreversible/non-atomic. | Upgrade sequencing or generic rollback expectations can fail across stores. | Require pre-change backup, pending-migration review, explicit stop conditions, and dated restore evidence through [OI-004](../open-items.md#oi-004). |
| Oban jobs | History pruned after 30 days; orphan rescue after 120 minutes; cron/queues can be disabled. | Evidence of missed jobs can disappear and delayed rescue may exceed an unchosen reporting tolerance. | Monitor job age/failure before pruning, validate configuration, and align thresholds with [OI-002](../open-items.md#oi-002)/[OI-014](../open-items.md#oi-014). |
| Monthly reports | Scheduler runs hourly; send job allows one attempt. | One transient mail failure can leave the required report undelivered without retryable failure state. | Correct or replace the path and reconcile monthly output through [OI-014](../open-items.md#oi-014). |
| Deletion | Hosted page claims 30-day backup retention post-cutoff; CE source cleanup worker is not in the self-host cron schedule. | Deletion completion/backup expiry can exceed policy if unowned or unscheduled. | Set option-specific lifecycle expectations and verify completion through [OI-008](../open-items.md#oi-008). |
| Certificates/secrets/service accounts | CE source can automate TLS when configured and accepts secret-file/environment values. | Certificate, password, token, geolocation, mail, S3, registry, or DNS expiry can interrupt collection/reporting. | Maintain redacted expiry/rotation inventory with primary/successor owners through [OI-001](../open-items.md#oi-001)/[OI-015](../open-items.md#oi-015). |
| Hosted subscription/terms | Nonpayment can restrict access; plan/price/service terms may change; cancellation makes stats inaccessible after the paid period. | Procurement or billing lapse can become a reporting/exit outage. | Assign billing/procurement successor, export cadence, renewal checkpoints, and termination plan through [OI-015](../open-items.md#oi-015). |

Evidence: [E-029](../../evidence/evidence-ledger.md#e-029), [E-035](../../evidence/evidence-ledger.md#e-035)–[E-039](../../evidence/evidence-ledger.md#e-039).

## Material Unknowns And Closure Routes

The library's actual calendar, owners, thresholds, and provider terms remain unknown. This view identifies control categories; it is not an operator aid or maintenance schedule.
