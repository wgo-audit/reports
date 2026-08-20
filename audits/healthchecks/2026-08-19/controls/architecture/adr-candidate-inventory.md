# Architecture Decision Candidate Inventory

## Evidence Boundary

This inventory covers source and configuration at `HC-CODE-001` commit
`fafac59eeb00cfdc87166242544fa071ecad1723`, plus repository operator
documentation effective at that commit. Implementation is observed; Acme's live
deployment, approval, ownership, workload behavior, and rationale are unknown.
Evidence is registered in [`evidence/evidence-ledger.md`](../../evidence/evidence-ledger.md).

## Coverage Domains

| Domain | Evidence boundary | Candidate count | Limitation/closure |
|---|---|---:|---|
| Components and contracts | Django application composition, route tables, models, and API documentation | 3 | Consumer adoption and compatibility needs are unknown; use OI-001 before changing client contracts. |
| Monitoring state and jobs | Ping ingestion, schedule calculation, database transitions, alert worker, and tests | 2 | Live timing and provider behavior require OI-006. |
| Runtime and deployment | Dockerfile, Compose, uWSGI, release workflow, and operator guidance | 2 | Acme topology and ownership require OI-005; no live environment was approved. |
| Data and provenance | Relational models, optional object storage, pruning, and migrations | 2 | Live engine, stored data, retention execution, restore, and applied migrations are unknown; OI-007 governs self-hosting. |
| Trust and dependency boundaries | Environment-based secrets, project API keys, public ping identifiers, and integration adapters | 1 | Security effectiveness and Acme controls are outside this review; route to Security and Privacy and OI-004. |

## Decision Candidates

| Candidate ID | Decision or durable behavior | Domain | Evidence | Observed/approved status | Disposition | Record or closure |
|---|---|---|---|---|---|---|
| AC-001 | Accounts, API, front end, payments, and notification adapters compose into one Django application and share ORM domain models. | Components | [E-006](../../evidence/evidence-ledger.md#E-006) | Observed implementation; approval and rationale unknown | inventory-only | Component relationships are shown in [component-and-contract-topology](diagrams/component-and-contract-topology.md); downstream change review must treat shared models as coupling points. |
| AC-002 | Management API v1, v2, and v3 share route handlers and version-aware model serialization. | Contracts | [E-006](../../evidence/evidence-ledger.md#E-006) | Observed and documented; consumer use and approval unknown | inventory-only | Code Quality and Product Value should verify compatibility risk before interface changes; OI-001 supplies Acme consumers. |
| AC-003 | UUID/slug ping URLs form a separate identifier-based ingress contract; slug pings can auto-provision checks and attach all project channels. | Contract/trust | [E-002](../../evidence/evidence-ledger.md#E-002), [E-006](../../evidence/evidence-ledger.md#E-006) | Observed implementation; live exposure and approval unknown | routed | Security and Privacy owns exposure analysis; Product Value owns workflow fit. |
| AC-004 | HTTP and SMTP signals converge on a database-serialized `Check`/`Ping` state transition and create durable `Flip` records. | Monitoring state | [E-002](../../evidence/evidence-ledger.md#E-002) | Observed implementation; live behavior and approval unknown | record-created | [ADR-001](adr/ADR-001-database-mediated-alert-state.md) |
| AC-005 | `sendalerts` polls the database, claims a flip by marking it processed before asynchronous channel delivery, and records delivery errors without a durable flip redelivery state. | Alert job | [E-003](../../evidence/evidence-ledger.md#E-003) | Observed implementation and source-test intent; live latency unknown | record-created | [ADR-001](adr/ADR-001-database-mediated-alert-state.md); verification [OI-006](../open-items.md#OI-006). |
| AC-006 | The supplied Docker topology has one database and one web service; uWSGI starts migrations and attaches alert/report/SMTP daemons. | Runtime/deployment | [E-004](../../evidence/evidence-ledger.md#E-004) | Observed reference configuration; not an observed Acme deployment | record-created | [ADR-002](adr/ADR-002-reference-container-process-coupling.md); decision [OI-005](../open-items.md#OI-005). |
| AC-007 | Release publication builds multi-architecture container images and emits an SBOM, while deployment version pinning remains an operator choice. | Delivery/dependency | [E-004](../../evidence/evidence-ledger.md#E-004) | Observed workflow; successful publication and Acme consumption unknown | inventory-only | Project Health and Maintenance Cost should evaluate release provenance and upgrade practice; OI-007 requires pinned self-host releases. |
| AC-008 | The relational database is the state authority; optional S3-compatible storage holds ping bodies over 100 bytes, with pruning spanning both stores. | Data/provenance | [E-005](../../evidence/evidence-ledger.md#E-005) | Observed implementation; live configuration and rationale unknown | record-created | [ADR-003](adr/ADR-003-relational-state-and-optional-object-bodies.md) |
| AC-009 | Startup applies pending migrations before the application; history contains data-transforming and destructive migrations. | Migration/runtime | [E-008](../../evidence/evidence-ledger.md#E-008) | Observed implementation; applied state, backup, and rollback unknown | routed | Captured in [ADR-002](adr/ADR-002-reference-container-process-coupling.md); action [OI-007](../open-items.md#OI-007). |
| AC-010 | Secrets and integration credentials are environment/file sourced; notification adapters are selected dynamically by channel kind. | Trust/dependency | [E-006](../../evidence/evidence-ledger.md#E-006) and `HC-CODE-001:hc/settings.py:55-79,315-371`; `HC-CODE-001:hc/api/models.py:47-75,1135-1184` | Observed implementation; live secret store, rotation, access, and provider configuration unknown | routed | Security and Privacy owns control assessment; OI-004 preserves unavailable Acme requirements. |
