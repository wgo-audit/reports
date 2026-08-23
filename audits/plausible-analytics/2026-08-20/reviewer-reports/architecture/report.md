# Architecture

## Audit Question, Depth, And Evidence Boundary

This detailed review asks whether the current technical boundary and its material decisions are understood well enough for safe change and a Run/Subscribe/Replace decision. The cutoff is 2026-08-20 at onboarding start, America/Toronto. Evidence is the approved `primary-code` snapshot at commit `9cc669b97ece3ecd37fcb3950791cb3873d7944d`, its repository documentation/configuration/workflows, and one explicitly post-cutoff public-page validation. No library deployment, live traffic, load test, internal/hosted system, contract, staff interview, legal conclusion, or separate Community Edition repository was inspected.

CodeGraph status/sync and topology exploration were used for navigation; its index covered the supported TypeScript/JavaScript/YAML surface, so Elixir source was inspected directly. No dependency was installed and no product test was run.

## Coverage And Material Gaps

Coverage includes tracker contracts, Phoenix endpoints and supervision, PostgreSQL/ClickHouse authority, event/session ingestion, background jobs, configuration/secrets, optional dependencies, container/release source, and cross-store migrations. The deployed CE version/topology is open in [OI-001](../../controls/open-items.md#oi-001); acceptable loss/outage tolerance in [OI-002](../../controls/open-items.md#oi-002); representative ingestion failure behavior in [OI-003](../../controls/open-items.md#oi-003); and deployment/migration/recovery proof in [OI-004](../../controls/open-items.md#oi-004).

## Key Findings

| Finding | Severity | Effort | Evidence links | Confidence and limitation | Consequence | Taxonomy |
|---|---|---|---|---|---|---|
| Architecture evidence supports only a conditional option comparison: the deployed Run topology is unknown, CE source cannot establish hosted architecture for Subscribe, and no replacement source was approved. | High | M | [E-001](../../evidence/evidence-ledger.md#e-001), [E-003](../../evidence/evidence-ledger.md#e-003), [E-007](../../evidence/evidence-ledger.md#e-007), [decision readiness](../../controls/architecture/adr-candidate-inventory.md#run--subscribe--replace-decision-readiness) | High confidence in evidence boundary; option-specific live evidence absent. | Selecting an option on unverified topology or cross-option inference could create unsupported reliability and operating-burden claims. | none |
| The reviewed embedded ingestion path returns HTTP 202 after casting rows to in-process buffers and before the reviewed ClickHouse write call; storage durability and actual loss behavior are unverified. | High | M | [E-004](../../evidence/evidence-ledger.md#e-004), [ADR-004](../../controls/architecture/adr/ADR-004-buffered-event-ingestion.md), [diagram](../../controls/architecture/diagrams/event-ingestion-and-durability-boundary.md) | High confidence in source ordering; no claim that production loss occurred or about its magnitude. | An abrupt failure could affect completeness of high-demand service measurements unless the deployed backend/configuration meets an explicit loss tolerance. | none |
| PostgreSQL and ClickHouse are separate authorities with cross-store migration dependencies and distinct operational lifecycles. | Medium | M | [E-003](../../evidence/evidence-ledger.md#e-003), [E-005](../../evidence/evidence-ledger.md#e-005), [ADR-001](../../controls/architecture/adr/ADR-001-dual-store-data-authority.md), [ADR-006](../../controls/architecture/adr/ADR-006-interwoven-cross-store-migrations.md) | High implementation confidence; deployed schemas, versions, backups, and migration execution unknown. | Run requires coordinated backup, upgrade, observability, and recovery across both stores; partial migration can create incompatible state. | none |
| CE and hosted/enterprise behavior diverge at build time and runtime; `master` is not evidence of the deployed CE release or hosted service. | Medium | M | [E-003](../../evidence/evidence-ledger.md#e-003), [E-007](../../evidence/evidence-ledger.md#e-007), [ADR-002](../../controls/architecture/adr/ADR-002-build-time-ce-and-ee-variants.md) | High source confidence; exact image digest and hosted implementation unknown. | Feature, clustering, filtering, and integration assumptions can be wrong if evidence is transferred across variants. | none |
| Jobs, reports, exports/imports, maintenance, secrets, and optional integrations add PostgreSQL and external dependency boundaries that are configurable but not inventoried for the library. | Medium | M | [E-006](../../evidence/evidence-ledger.md#e-006), [ADR-005](../../controls/architecture/adr/ADR-005-postgresql-backed-background-jobs.md), [ADR-007](../../controls/architecture/adr/ADR-007-runtime-configuration-and-secret-files.md) | High confidence in source configuration surface; enabled set, owners, health, and controls unknown. | Monthly reporting or maintenance can degrade independently of collection, and unowned integrations expand operational/security burden. | none |

## Mandate-Relevant Strengths

- The source has a legible separation between application state and analytics workloads, reducing ambiguity for datastore-specific review ([E-001](../../evidence/evidence-ledger.md#e-001), [E-003](../../evidence/evidence-ledger.md#e-003)).
- Cross-store migration ordering is explicitly encoded and explained, rather than leaving repository order implicit ([E-005](../../evidence/evidence-ledger.md#e-005)).
- Tracker variants share a documented source and contract surface, supporting consistent implementation when deployment/version control is disciplined ([E-002](../../evidence/evidence-ledger.md#e-002)).
- Runtime configuration validates required key material and supports secret-file injection; this is a useful mechanism, though not proof of library governance ([E-006](../../evidence/evidence-ledger.md#e-006)).

### Decision Insights

1. **Run readiness depends on a declared measurement-loss tolerance, not traffic volume alone.** Batching makes collection efficient but creates an acknowledgement-to-write interval. A wrong assumption can overstate the completeness of registration/seasonal reporting. Set [OI-002](../../controls/open-items.md#oi-002), then test representative failure behavior through [OI-003](../../controls/open-items.md#oi-003).
2. **The Run/Subscribe comparison must use option-specific operations evidence.** Shared source does not erase CE/hosted build and responsibility differences. A wrong cross-option inference can assign high availability, backups, or controls to the wrong party. Close Run topology through [OI-001](../../controls/open-items.md#oi-001); hosted reviewers need hosted-service evidence.
3. **Upgrade safety is a dual-store continuity decision.** Interwoven migrations encode cross-store dependencies, so a single-database backup or generic container rollback is insufficient evidence. Review the exact deployed CE release/runbook and recovery path through [OI-004](../../controls/open-items.md#oi-004).

## Selected Outputs

- [ADR candidate inventory](../../controls/architecture/adr-candidate-inventory.md)
- [ADR register](../../controls/architecture/adr-register.md) and seven linked observed-decision records
- [Component and data-authority view](../../controls/architecture/diagrams/component-and-data-authority-view.md)
- [Event ingestion and durability-boundary view](../../controls/architecture/diagrams/event-ingestion-and-durability-boundary.md)
- [Deployment and runtime path](../../controls/architecture/diagrams/deployment-and-runtime-path.md)

A live DevOps infrastructure view was not triggered because no approved live-environment evidence exists. The selected outputs passed one independent artifact-quality review and were revised once to correct option readiness, domain accounting, and durability wording.

## Material Omissions, Unknowns, And Auditor Questions

The material auditor question is routed through [OI-002](../../controls/open-items.md#oi-002): **What maximum event-loss window and dashboard/reporting outage are acceptable during high-demand library services?** This is an acceptance/authority question that can change whether Run is architecture-ready. Deployment version/topology, failure behavior, and migration/recovery are proof needs routed as verifications, not questions.

Documented outside audited scope; not independently verified. The main repository and approved public page point to a separate Community Edition source for installation material. The smallest useful expansion is that repository at the deployed tag plus the library's redacted deployment/upgrade/rollback material, as recorded in [OI-004](../../controls/open-items.md#oi-004).

## Reconciliation

This is a fresh audit with no prior Architecture outputs or open items. No material conflict was found between the cutoff-bounded repository evidence and the post-cutoff public-page validation; the latter was not used to change cutoff state. Source implementation and public claims were not treated as live operation, approval, cost, or hosted-service proof.

## Bounded Conclusion And Downstream Guidance

The approved source is architecturally understandable: a shared tracker and Phoenix application feed an in-process session/ingestion pipeline, PostgreSQL holds application/jobs state, ClickHouse holds analytical data, and migrations coordinate both stores. That is enough for downstream Product Value, Security/Privacy, Code Quality, Business Continuity, Cloud Security, Expense, Scalability, and Maintenance reviewers to use the linked source boundaries. It is not enough to declare Run dependable, Subscribe equivalent, or Replace preferable. Downstream reviewers must not assume that source topology proves deployed version, live configuration, capacity, durability, recovery, ownership, or hosted controls.
