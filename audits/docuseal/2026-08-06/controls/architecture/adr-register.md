# Architecture Decision Register

## Evidence Boundary

Records below capture source-backed decisions or durable behaviors in DocuSeal Community `3.1.7`. `Observed` does not mean approved, operated, or suitable for the organization's target architecture.

## Records

| ID | Statement | Domain | Status | Evidence confidence | Record link |
|---|---|---|---|---|---|
| ADR-001 | Rails modular monolith with ERB/Turbo/Vue UI boundaries | Component | observed | High for source topology; live ownership unknown | [Record](adr/ADR-001-modular-monolith-and-ui-boundary.md) |
| ADR-002 | Implicit template/signer contracts and conditional snapshots | Contracts | observed | High for source behavior; compatibility unknown | [Record](adr/ADR-002-internal-template-and-signer-contracts.md) |
| ADR-003 | Community, hosted/OpenAPI, Pro embedding and extension boundaries differ | Contracts/edition | observed | High for Community boundary; Pro/entitlement unknown | [Record](adr/ADR-003-edition-specific-integration-boundary.md) |
| ADR-004 | Webhooks are asynchronous HMAC-signed at-least-once-style delivery | Contracts/jobs | observed | High for implementation; live consumer behavior unknown | [Record](adr/ADR-004-webhook-delivery-contract.md) |
| ADR-005 | SQL owns workflow metadata and Active Storage owns bytes | Data/lifecycle | observed | High for source; target authority/retention unknown | [Record](adr/ADR-005-data-and-file-authority.md) |
| ADR-006 | Completion crosses SQL into embedded-capable Sidekiq/Redis processing | Jobs/runtime | observed | High for topology; recovery/capacity unknown | [Record](adr/ADR-006-completion-and-job-topology.md) |
| ADR-007 | Signing, audit snapshots and verification are configuration-dependent | Critical pipeline/trust | observed | High for code path; trust/specialist acceptance unknown | [Record](adr/ADR-007-signing-audit-and-verification-trust.md) |
| ADR-008 | Production boot is coupled to database migration | Release/configuration | observed | High for initializer/migration; target rollout unknown | [Record](adr/ADR-008-boot-coupled-database-migrations.md) |
| ADR-009 | Container/runtime example couples mutable images, ingress and state | Runtime/deployment | observed | High for shipped files; live state unknown | [Record](adr/ADR-009-container-runtime-boundary.md) |
| ADR-010 | Identity, tokens and encrypted records share application secret roots | Identity/secrets | observed | High for source; target custody/rotation unknown | [Record](adr/ADR-010-identity-and-secret-root-boundary.md) |
| ADR-011 | Tag-triggered image publication lacks demonstrated promotion provenance | Release/dependencies | observed | High for workflow/run; deployed digest unknown | [Record](adr/ADR-011-release-image-provenance-and-promotion.md) |

## Coverage And Disposition

| Primary domain | Candidates | Records | Other dispositions | Limitation |
|---|---:|---:|---|---|
| Component | 2 | 1 | 1 merged | No target ownership/decomposition evidence. |
| Runtime/deployment | 2 | 1 | 1 merged | No live environment or target topology. |
| Release/configuration | 1 | 1 | none | Approval and rollback unproved. |
| Identity/secrets | 2 | 1 | 1 merged | Pro identity and specialist trust decisions unavailable. |
| Data authority/lifecycle | 2 | 1 | 1 merged | Backup, retention, residency and deletion policy unknown. |
| Jobs | 1 | 1 | none | Queue durability/recovery unobserved. |
| Contracts | 6 | 3 | 2 merged, 1 deferred | Edition compatibility and consumer acceptance unknown. |
| Dependencies | 1 | 1 | none | SBOM/vulnerability/deployed provenance not established. |
| Capacity/cost | 1 | 0 | 1 blocked | Target workload and cost model absent. |
| Critical pipeline | 1 | 1 | none | Correctness, immutable preservation and specialist acceptance unproved. |
| Runtime/operations | 1 | 0 | 1 blocked | Telemetry, SLO, alert and ownership proof absent. |
