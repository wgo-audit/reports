# ADR-006: Interwoven Cross-Store Migrations

- Status: observed
- Evidence cutoff: 2026-08-20 at onboarding start, America/Toronto

## Decision Statement

Release migration logic merges pending PostgreSQL and ClickHouse migrations into version-ordered repository streaks rather than migrating each store independently.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Implementation | `interweave_migrate/0` orders cross-repository dependencies; PR workflow separates migrations from app/config changes. | [E-005](../../../evidence/evidence-ledger.md#e-005) | Hosted workflow execution and deployed migration state unverified. |
| Runtime/live state | unknown | [OI-004](../../../controls/open-items.md#oi-004) | No runbook/history or database access. |
| Rationale | Source documentation explains that independent repo migration can violate cross-store ordering. | [E-005](../../../evidence/evidence-ledger.md#e-005) | No library-specific acceptance. |
| Approval | unknown | [OI-004](../../../controls/open-items.md#oi-004) | Upgrade authority/procedure unavailable. |

## Constraints, Options, And Tradeoffs

Ordering protects known cross-store dependencies, but increases the importance of exact release tooling, compatible store versions, pre-change backups, and defined rollback/recovery boundaries.

## Impacts And Boundaries

Skipping the intended migrator or partial failure can create cross-store incompatibility. The source does not establish that library upgrades invoke it correctly.

## Change, Reversal, And Follow-Up

Review the deployed CE release procedure, applied state, backup prerequisite, and recovery evidence through [OI-004](../../../controls/open-items.md#oi-004).
