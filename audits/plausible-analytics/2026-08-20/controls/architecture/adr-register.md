# Architecture Decision Register

`observed` means implemented or documented in the approved source snapshot; it does not mean approved by the library or verified in operation.

## Records

| ID | Statement | Domain | Status | Evidence confidence | Record link |
|---|---|---|---|---|---|
| ADR-001 | Split general/application state from analytics data across PostgreSQL and ClickHouse. | Data authority/components | observed | High for source; unknown live | [Record](adr/ADR-001-dual-store-data-authority.md) |
| ADR-002 | Build CE and hosted/enterprise variants from one monorepo with compile-time boundaries. | Runtime/release | observed | High for source; unknown approval/live | [Record](adr/ADR-002-build-time-ce-and-ee-variants.md) |
| ADR-003 | Compile tracker targets from a shared source and serve site-specific configuration. | Components/contracts | observed | High for source; unknown deployment | [Record](adr/ADR-003-single-source-tracker-variants.md) |
| ADR-004 | Buffer accepted events and sessions in-process before the reviewed ClickHouse write attempt. | Data provenance | observed | High for source; impact/durability unverified | [Record](adr/ADR-004-buffered-event-ingestion.md) |
| ADR-005 | Use PostgreSQL-backed Oban for scheduled and asynchronous work. | Jobs | observed | High for source; unknown live health | [Record](adr/ADR-005-postgresql-backed-background-jobs.md) |
| ADR-006 | Interweave PostgreSQL and ClickHouse migrations by version. | Migrations | observed | High for implementation; unknown execution | [Record](adr/ADR-006-interwoven-cross-store-migrations.md) |
| ADR-007 | Load runtime configuration/secrets from environment or files and conditionally enable integrations. | Identity/secrets/dependencies | observed | High for source; unknown live configuration | [Record](adr/ADR-007-runtime-configuration-and-secret-files.md) |

## Coverage And Disposition

| Domain | Candidates | Records | Other dispositions | Limitation |
|---|---:|---:|---|---|
| Components/contracts | 1 | 1 | 0 | Deployed scripts/proxies unknown. |
| Runtime/deployment/release | 3 | 1 | 1 merged; 1 blocked | Separate CE deployment source and live topology not approved. |
| Identity/secrets/dependencies | 2 | 1 | 1 merged | Enabled integrations/provider unknown. |
| Data authority/provenance | 2 | 2 | 0 | Live schema/retention/correctness unknown. |
| Jobs | 1 | 1 | 0 | Queue health/ownership unknown. |
| Migrations | 1 | 1 | 0 | Applied state/rollback evidence unknown. |
| Capacity/cost | 1 | 0 | 1 deferred | No acceptance threshold or live sizing evidence. |
