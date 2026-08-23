# Architecture Decision Register

Reader question: Which observed architecture records exist, and how completely were decision domains covered?

This is an audit reconstruction, not proof that Plausible approved these records. All records are `observed`; approval and current production operation remain unknown unless explicitly stated.

## Safe-Change Boundary

`[Verified audit conclusion]` Source-local component and configuration behavior is evidenced sufficiently for targeted code navigation. Any change whose safety depends on release/promotion, persistence durability, cross-store deletion convergence, production topology, or approval authority must first close the corresponding [material open item](../open-items.md).

## Records

| ID | Statement | Domain | Status | Evidence confidence | Record link |
|---|---|---|---|---|---|
| ADR-001 | CE and cloud/EE are compile-time build profiles of one monorepo application. | Component/build | observed | High for source; unknown for live profile inventory | [record](adr/ADR-001-compile-time-ce-and-cloud-build-profiles.md) |
| ADR-002 | PostgreSQL holds relational/control/job state and ClickHouse holds analytics data behind specialized repositories and interwoven migrations. | Data/migrations | observed | High for source; unknown for deployed schemas | [record](adr/ADR-002-postgresql-control-and-clickhouse-analytics-stores.md) |
| ADR-003 | Ingestion uses pluggable embedded/remote persistence, deterministic rollout, session cache, and asynchronous write buffering. | Ingestion/runtime | observed | High for source; unknown for live selection and durability | [record](adr/ADR-003-asynchronous-pluggable-ingestion-persistence.md) |
| ADR-004 | Scheduled and asynchronous work uses PostgreSQL-backed Oban. | Jobs/runtime | observed | High for configuration; unknown for live health | [record](adr/ADR-004-postgresql-backed-oban-work-scheduling.md) |
| ADR-005 | Tracker integrations are built from one source into web, legacy, npm, and support variants. | Client/contracts | observed | High for source; unknown for publication/runtime compatibility | [record](adr/ADR-005-single-source-multi-variant-tracker.md) |
| ADR-006 | GitHub Actions builds container artifacts for cloud and CE; cloud promotion remains an external/unknown handoff. | Delivery/deployment | observed | High for workflow and hosted run; low for deployment | [record](adr/ADR-006-container-image-build-boundary.md) |
| ADR-007 | A PostgreSQL worklist hands site deletion to an asynchronous ClickHouse cleanup worker. | Data deletion | observed | High for source/history; unknown for live convergence | [record](adr/ADR-007-postgresql-worklist-for-clickhouse-site-deletion.md) |

## Coverage And Disposition

| Domain | Candidates | Records | Other dispositions | Limitation |
|---|---:|---:|---|---|
| Component/build | 2 | 1 | 1 merged | Live topology and ownership unknown. |
| Data authority/migrations | 2 | 1 | 1 merged | Deployed schema/migration state unknown. |
| Ingestion/sessions | 2 | 1 | 1 merged | Production persistence and loss envelope unknown. |
| Jobs | 1 | 1 | 0 | Queue operation and outcomes unknown. |
| Tracker/contracts | 2 | 1 | 1 deferred | Public support/version decisions need Product Value evidence. |
| Delivery/observability | 2 | 1 | 1 merged | Promotion, runtime, and monitoring operation unknown. |
| Cross-store deletion | 1 | 1 | 0 | Completion and reconciliation unknown. |
| Identity/secrets | 1 | 0 | 1 deferred | Downstream security reviewers own control assurance. |
| Governance | 1 | 0 | 1 blocked | Approval/rationale baseline requires [OI-005](../open-items.md#oi-005). |
