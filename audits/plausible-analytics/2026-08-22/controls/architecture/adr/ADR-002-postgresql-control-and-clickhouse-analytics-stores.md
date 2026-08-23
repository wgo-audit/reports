# ADR-002: PostgreSQL Control and ClickHouse Analytics Stores

- Status: observed
- Evidence cutoff: 2026-08-22 22:08:28 EDT

## Decision Statement

`[Verified fact]` PostgreSQL holds relational/control data and Oban jobs; ClickHouse holds analytics data behind distinct read-only, buffered-ingest, async-insert, and deletion repositories. Cross-store schema changes are ordered by a custom interwoven migrator. [E-004](../../../evidence/evidence-ledger.md#e-004)

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Implementation | `Plausible.Repo` and specialized ClickHouse repos are supervised; 235 PostgreSQL, 55 ClickHouse, and 45 data-migration files are present. | E-001, E-004 | Source count does not prove deployed state. |
| Runtime/live state | `[Unknown]` Deployed versions, topology, replication, lag, and migration history. | [OI-003](../../open-items.md#oi-003) | No production access. |
| Rationale | `[Verified fact]` `interweave_migrate/0` documents cross-repository dependency ordering; ClickHouse query/write/delete settings separate workload types. | E-004 | Broader capacity/cost rationale is not recorded. |
| Approval | `[Unknown]` | [OI-005](../../open-items.md#oi-005) | No attributed authority record. |

## Constraints, Options, And Tradeoffs

`[Reasoned inference]` The split matches relational control and analytical query/write workloads, while cross-store operations cannot rely on one database transaction. The custom migrator and migration-only PR gate are explicit mitigations; deletion needs a separate convergence contract (ADR-007).

## Impacts And Boundaries

Application changes can require ordered migrations across two engines. Read, ingest, async-insert, and deletion pools have different semantics. This record does not establish backup, restore, replica, retention, or production failover behavior.

## Change, Reversal, And Follow-Up

Verify release migration gates through [OI-003](../../open-items.md#oi-003) and deletion convergence through [OI-002](../../open-items.md#oi-002).
