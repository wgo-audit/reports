# Architecture Decision Candidate Inventory

## Source Boundary

This inventory covers the approved `primary-code` snapshot at commit `9cc669b97ece3ecd37fcb3950791cb3873d7944d` and one post-cutoff public-page validation. It distinguishes source-observed behavior from approval and live operation. The library deployment, separate Community Edition deployment repository, contracts, and non-public hosted systems were not inspected.

## Run / Subscribe / Replace Decision Readiness

Architecture evidence supports only a conditional comparison. **Run** should not be treated as architecture-ready until [OI-001](../../controls/open-items.md#oi-001) through [OI-004](../../controls/open-items.md#oi-004) establish the deployed topology, acceptable loss/outage threshold, representative ingestion failure behavior, and deployment/migration/recovery path. CE source cannot establish the hosted service's live architecture or controls for **Subscribe**. No replacement product/source was approved, so Architecture cannot assess **Replace**. The stop condition is therefore: do not select an option on architecture claims that its option-specific evidence cannot support.

## Coverage Domains

| Domain | Evidence boundary | Candidate count | Limitation/closure |
|---|---|---:|---|
| Components and contracts | Tracker, Phoenix endpoint/router, dashboard client, APIs | 1 | Deployed tracker versions and proxy paths require [OI-001](../../controls/open-items.md#oi-001). |
| Runtime/deployment and release | OTP tree, Dockerfile, tagged public-image workflow | 3 | Image publication is not deployment proof; [OI-001](../../controls/open-items.md#oi-001) and [OI-004](../../controls/open-items.md#oi-004). |
| Identity, secrets, configuration | Runtime environment/file configuration and vault keys | 1 | Actual secret store and enabled integrations require [OI-001](../../controls/open-items.md#oi-001). |
| Data authority and provenance | PostgreSQL, ClickHouse, ingestion/session pipeline | 2 | Live schemas, versions, retention, and data correctness unknown. |
| Jobs | Oban queues, cron, PostgreSQL peer/pruner | 1 | Live queue ownership and health unknown. |
| Migrations | Interwoven cross-store migration implementation and PR guard | 1 | Applied state, backup, rollback, and runbook require [OI-004](../../controls/open-items.md#oi-004). |
| Dependencies | Mail, geolocation, S3, telemetry, Google and other optional services | 1 | Enabled set and failure handling unknown; merged into configuration boundary. |
| Capacity/cost | Source buffer, pool, timeout, and queue knobs | 1 | No live sizing or peak evidence; [OI-001](../../controls/open-items.md#oi-001), [OI-002](../../controls/open-items.md#oi-002), and [OI-003](../../controls/open-items.md#oi-003). |

## Decision Candidates

| Candidate ID | Decision or durable behavior | Domain | Evidence | Observed/approved status | Disposition | Record or closure |
|---|---|---|---|---|---|---|
| ARCH-DC-001 | General application state and jobs use PostgreSQL while analytics events/sessions and stats queries use ClickHouse-specific repos. | Data authority/components | [E-001](../../evidence/evidence-ledger.md#e-001), [E-003](../../evidence/evidence-ledger.md#e-003), [E-006](../../evidence/evidence-ledger.md#e-006) | observed; approval and live use unknown | record-created | [ADR-001](adr/ADR-001-dual-store-data-authority.md) |
| ARCH-DC-002 | CE and hosted/enterprise behaviors are selected partly at build time from one monorepo, with further self-host/runtime branching. | Runtime/release | [E-003](../../evidence/evidence-ledger.md#e-003), [E-007](../../evidence/evidence-ledger.md#e-007) | observed; rationale partly documented; approval unknown | record-created | [ADR-002](adr/ADR-002-build-time-ce-and-ee-variants.md) |
| ARCH-DC-003 | A single tracker source compiles many web, legacy, and NPM variants and receives site-specific configuration from the application endpoint. | Components/contracts | [E-002](../../evidence/evidence-ledger.md#e-002) | observed; design goals documented; deployment unknown | record-created | [ADR-003](adr/ADR-003-single-source-tracker-variants.md) |
| ARCH-DC-004 | Event requests are accepted after synchronous validation/session processing and asynchronous casts into in-process ClickHouse write buffers. | Data provenance | [E-004](../../evidence/evidence-ledger.md#e-004) | observed; loss tolerance and approval unknown | record-created | [ADR-004](adr/ADR-004-buffered-event-ingestion.md) |
| ARCH-DC-005 | Scheduled and asynchronous work uses PostgreSQL-backed Oban with self-host and cloud queue/cron variants. | Jobs | [E-006](../../evidence/evidence-ledger.md#e-006) | observed; live enablement/health unknown | record-created | [ADR-005](adr/ADR-005-postgresql-backed-background-jobs.md) |
| ARCH-DC-006 | Pending PostgreSQL and ClickHouse migrations are interwoven by version to honor cross-store dependencies. | Migrations | [E-005](../../evidence/evidence-ledger.md#e-005) | observed; operational approval/execution unknown | record-created | [ADR-006](adr/ADR-006-interwoven-cross-store-migrations.md) |
| ARCH-DC-007 | Runtime configuration and secrets can be supplied through environment variables or files below a configurable secrets directory; integrations are conditionally enabled. | Identity/secrets/dependencies | [E-006](../../evidence/evidence-ledger.md#e-006) | observed; live provider and ownership unknown | record-created | [ADR-007](adr/ADR-007-runtime-configuration-and-secret-files.md) |
| ARCH-DC-008 | Tagged source builds multi-architecture CE container images in GHCR. | Release/deployment | [E-007](../../evidence/evidence-ledger.md#e-007) | observed source workflow; hosted execution and deployment unknown | merged-into | ADR-002 covers the material release/build boundary; validate deployed digest through [OI-001](../../controls/open-items.md#oi-001). |
| ARCH-DC-009 | Optional mail, geolocation, S3, telemetry, Google, and support integrations extend the runtime trust/dependency boundary. | Dependencies | [E-006](../../evidence/evidence-ledger.md#e-006) | observed configuration surface; live use unknown | merged-into | ADR-007; inventory enabled integrations through [OI-001](../../controls/open-items.md#oi-001). |
| ARCH-DC-010 | Buffer sizes, flush intervals, pool sizes, query timeouts, and job concurrency are configurable capacity controls. | Capacity/cost | [E-003](../../evidence/evidence-ledger.md#e-003), [E-004](../../evidence/evidence-ledger.md#e-004), [E-006](../../evidence/evidence-ledger.md#e-006) | observed knobs; adequacy and cost unknown | deferred | Determine acceptance threshold in [OI-002](../../controls/open-items.md#oi-002), then validate through [OI-001](../../controls/open-items.md#oi-001) and [OI-003](../../controls/open-items.md#oi-003). |
| ARCH-DC-011 | The main repository points to a separate Community Edition source for installation material; that source's deployment and upgrade content was not inspected. | Deployment/dependency | [E-001](../../evidence/evidence-ledger.md#e-001), [E-008](../../evidence/evidence-ledger.md#e-008) | documented pointer; external source unverified | blocked | Documented outside audited scope; not independently verified. Close through [OI-004](../../controls/open-items.md#oi-004). |
