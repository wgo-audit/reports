# ADR-008: Boot-Coupled Database Migrations

- Status: observed
- Evidence cutoff: 2026-08-06

## Decision Statement

Production application preparation executes database migrations unless `RUN_MIGRATIONS=false`. The pinned connection configuration has no separate migration URL, and the migration set includes non-reversible/model-coupled data changes.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Implementation | Boot initializer calls migration; data backfill has no effective down path | [Data packet §11](../../../evidence/packets/architecture-data-jobs-migrations-provenance.md) | Release note timing is maintainer estimate, not target benchmark |
| Runtime/live state | unknown | No deployment/database observation | Replica coordination and pooled DB compatibility unknown |
| Rationale | unknown | No decision record found | Convenience is not proven intent |
| Approval | unknown | No release authority supplied | Maintenance/rollback policy unapproved |

## Constraints, Options, And Tradeoffs

Automatic boot migration simplifies single-instance upgrades but can race replicas and couples availability to DDL/data work. A dedicated single-run migration job with direct connectivity, expand/contract compatibility, backup/rehearsal and roll-forward/restore gates reduces ambiguity.

## Impacts And Boundaries

Release `3.1.3` documents volume-dependent startup impact; draft PR #691/issue #469 are leads only. Wrong assumptions can block startup or produce partial rollout.

## Change, Reversal, And Follow-Up

OI-004 must define and test the migration release process, including multi-replica coordination, timeout, post-check, backup, rollback/roll-forward and pooled/direct connection policy.
