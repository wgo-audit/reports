# ADR-001: Dual-Store Data Authority

- Status: observed
- Evidence cutoff: 2026-08-20 at onboarding start, America/Toronto

## Decision Statement

The source separates general application state and PostgreSQL-backed jobs from analytics event/session storage and queries in ClickHouse.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Implementation | OTP starts PostgreSQL plus read, ingest, async-insert, and deletion ClickHouse repos; Oban uses the PostgreSQL repo. | [E-003](../../../evidence/evidence-ledger.md#e-003), [E-006](../../../evidence/evidence-ledger.md#e-006) | Does not prove live topology or versions. |
| Runtime/live state | unknown | [OI-001](../../../controls/open-items.md#oi-001) | No library configuration/system access. |
| Rationale | README labels PostgreSQL “general data” and ClickHouse “analytics”; source specializes connection roles. | [E-001](../../../evidence/evidence-ledger.md#e-001), [E-003](../../../evidence/evidence-ledger.md#e-003) | No approval record or evaluated alternatives. |
| Approval | unknown | [OI-001](../../../controls/open-items.md#oi-001) | Source presence is not organizational approval. |

## Constraints, Options, And Tradeoffs

The split fits transactional account/configuration state and analytical query workloads, but creates two datastore lifecycles, backup regimes, observability surfaces, and cross-store change dependencies. Subscribe transfers much of that operating burden; Run retains it.

## Impacts And Boundaries

Loss, lag, or schema mismatch in either store can affect reports differently. Architecture establishes the split, not consistency, recovery, retention, or peak capacity.

## Change, Reversal, And Follow-Up

Changing stores is a broad migration. First inventory the deployed topology through [OI-001](../../../controls/open-items.md#oi-001) and validate recovery/migrations through [OI-004](../../../controls/open-items.md#oi-004).
