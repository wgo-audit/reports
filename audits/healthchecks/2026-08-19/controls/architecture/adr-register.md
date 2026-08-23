# Architecture Decision Register

## Evidence Boundary

Records describe observed durable source behavior at `HC-CODE-001` commit
`fafac59eeb00cfdc87166242544fa071ecad1723`. `observed` does not mean Acme
approved, deployed, or accepted the behavior.

## Records

| ID | Statement | Domain | Status | Evidence confidence | Record link |
|---|---|---|---|---|---|
| ADR-001 | Monitoring state and alert handoff are mediated by relational `Check`, `Ping`, and `Flip` records; a flip is claimed before delivery completes. | Monitoring state/jobs | observed | High for source structure; unknown for live latency and reliability | [ADR-001](adr/ADR-001-database-mediated-alert-state.md) |
| ADR-002 | The reference container starts migrations, web serving, alerting, reports, and optional SMTP under one uWSGI-managed runtime. | Runtime/deployment | observed | High for supplied configuration; none for Acme deployment | [ADR-002](adr/ADR-002-reference-container-process-coupling.md) |
| ADR-003 | Relational storage is authoritative and optional S3-compatible storage externalizes larger ping bodies with cross-store pruning. | Data/provenance | observed | High for implementation; none for live storage and recovery | [ADR-003](adr/ADR-003-relational-state-and-optional-object-bodies.md) |

## Coverage And Disposition

| Domain | Candidates | Records | Other dispositions | Limitation |
|---|---:|---:|---|---|
| Components and contracts | 3 | 0 | 2 inventory-only; 1 routed to Security/Product Value | Source establishes interfaces, not consumer use or approval. |
| Monitoring state and jobs | 2 | 1 | Both candidates consolidated into ADR-001 | No live fault or latency evidence; [OI-006](../open-items.md#OI-006). |
| Runtime and deployment | 2 | 1 | Release publication remains inventory-only | Reference configuration is not Acme topology; [OI-005](../open-items.md#OI-005). |
| Data and provenance | 2 | 1 | Migration candidate incorporated into ADR-002 | Live stores, applied migrations, backup, and restore are unknown; [OI-007](../open-items.md#OI-007). |
| Trust and dependencies | 1 | 0 | Routed to Security and Privacy | Acme security requirements and live configuration are unavailable; [OI-004](../open-items.md#OI-004). |

## Pull, Make, And Buy Decision Gate

| Option | Architecture gate | Stop condition |
|---|---|---|
| Pull | Close [OI-005](../open-items.md#OI-005), [OI-006](../open-items.md#OI-006), and [OI-007](../open-items.md#OI-007) with deployment controls outside a product fork where possible. | Do not approve self-hosting while the target topology, recovery controls, or measured five-minute path remains unproven. |
| Make | First test pull with the target operational controls; identify a source-level defect that still prevents the measurement contract, then record the fork design, ownership, and upgrade cost. | Do not fork merely to replace the sample deployment topology; fork only when evidence shows an application change is necessary and sustainable. |
| Buy | Close [OI-004](../open-items.md#OI-004) and obtain equivalent end-to-end T0/T1 evidence for the hosted path, including independent detection of vendor/notification failure. | Do not transfer self-hosted source claims to hosted internals or accept a contractual claim without evidence against the same five-minute boundary. |
