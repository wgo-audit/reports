# ADR-004: PostgreSQL-Backed Oban Work Scheduling

- Status: observed
- Evidence cutoff: 2026-08-22 22:08:28 EDT

## Decision Statement

`[Verified fact]` Scheduled and asynchronous work runs through Oban using PostgreSQL, with base/cloud cron and queues, Postgres peer election, pruning, lifeline rescue, reindexing, and error reporting. [E-008](../../../evidence/evidence-ledger.md#e-008)

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Implementation | `[Verified fact]` Runtime config defines base/cloud crontabs and queues; application supervises Oban. | [E-008](../../../evidence/evidence-ledger.md#e-008) | Configuration does not prove execution. |
| Runtime/live state | `[Unknown]` Backlog, latency, retry/dead jobs, cron leadership, and completion SLOs. | E-008 | No live queue evidence. |
| Rationale | `[Reasoned inference]` Reusing PostgreSQL provides durable queue state and cluster election without a separate broker. | E-004, E-008 | No source-attributed decision narrative. |
| Approval | `[Unknown]` | [OI-005](../../open-items.md#oi-005) | No approval record. |

## Constraints, Options, And Tradeoffs

`[Reasoned inference]` PostgreSQL is both a control-plane store and job-coordination dependency. `[Verified fact]` Queue concurrency is explicitly configured; capacity and operational outcomes belong to Scalability and Business Continuity.

## Impacts And Boundaries

`[Verified fact]` Source-visible work includes reports, imports/exports, deletion, billing/usage, cache purges, and housekeeping. `[Unknown]` Successful downstream business completion is not established by source configuration.

## Change, Reversal, And Follow-Up

Downstream reviewers should obtain queue health, retry policy, critical-job ownership, and completion monitors; do not infer them from this record.
