# ADR-005: PostgreSQL-Backed Background Jobs

- Status: observed
- Evidence cutoff: 2026-08-20 at onboarding start, America/Toronto

## Decision Statement

Scheduled and asynchronous application work uses Oban persisted through the PostgreSQL repo, with different self-host and cloud job sets.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Implementation | Cron, queues, pruner, lifeline, reindexer, and PostgreSQL peer are configured for production/CE. | [E-006](../../../evidence/evidence-ledger.md#e-006) | Actual enablement and queue state unknown. |
| Runtime/live state | unknown | [OI-001](../../../controls/open-items.md#oi-001) | No job dashboard/telemetry approved. |
| Rationale | Persistent jobs coordinate reports, exports/imports, cleaning, notifications, and maintenance. | [E-006](../../../evidence/evidence-ledger.md#e-006) | No formal alternatives/approval record. |
| Approval | unknown | [OI-001](../../../controls/open-items.md#oi-001) | Library ownership not evidenced. |

## Constraints, Options, And Tradeoffs

Reusing PostgreSQL avoids a separate broker but couples job availability and maintenance to the application database. Per-queue concurrency is source-configured and may need live validation for monthly reporting and seasonal work.

## Impacts And Boundaries

Job backlog can affect scheduled reports, exports, imports, cleanup, and notifications without necessarily stopping event ingestion.

## Change, Reversal, And Follow-Up

Inventory enabled queues, cron ownership, alerts, and backlog evidence through [OI-001](../../../controls/open-items.md#oi-001); Business Continuity should assess recovery.
