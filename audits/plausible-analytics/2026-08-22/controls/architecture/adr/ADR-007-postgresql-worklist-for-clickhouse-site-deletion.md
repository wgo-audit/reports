# ADR-007: PostgreSQL Worklist for ClickHouse Site Deletion

- Status: observed
- Evidence cutoff: 2026-08-22 22:08:28 EDT

## Decision Statement

`[Verified fact]` Site removal inserts a PostgreSQL pending-deletion row transactionally, then a weekly Oban worker finds ClickHouse partitions, issues asynchronous deletes, and clears the worklist row. [E-005](../../../evidence/evidence-ledger.md#e-005)

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Implementation | `[Verified fact]` PostgreSQL records intent; ClickHouse-derived partitions bound work; a dedicated deletion pool issues lightweight deletes and one mutation; completion is not awaited in production settings before clearing intent. | [E-005](../../../evidence/evidence-ledger.md#e-005) | Live settings/outcomes unknown. |
| Runtime/live state | `[Unknown]` Mutation success, residual rows, retry/reconciliation, backfill completion, and deletion latency. | [OI-002](../../open-items.md#oi-002) | No ClickHouse system tables or deletion records. |
| Rationale | `[Verified fact]` PR #6591 aimed to avoid expensive whole-table discovery/mutations and batch deletion; review changed unreliable PostgreSQL date-derived ranges to ClickHouse partition discovery. | [E-005](../../../evidence/evidence-ledger.md#e-005) | Linked internal Basecamp material unavailable. |
| Approval | `[Unknown]` beyond a final public PR approval. | E-005, [OI-005](../../open-items.md#oi-005) | PR approval is not organization-wide architecture approval. |

## Constraints, Options, And Tradeoffs

`[Reasoned inference]` The worklist reduces repeated full-store discovery and isolates deletion load, but clearing intent after asynchronous issuance weakens durable completion semantics. PR review explicitly challenged convergence and identified race/residual cases; the final description retains a spanning-session edge as negligible and limits mutation monitoring.

## Impacts And Boundaries

This is a cross-store data lifecycle boundary with customer/privacy consequences. The source does not prove a live deletion failure; it establishes that completion and reconciliation must be separately evidenced.

## Change, Reversal, And Follow-Up

Close [OI-002](../../open-items.md#oi-002) before asserting deletion convergence or accepting the current semantics as sufficient.
