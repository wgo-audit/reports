# Architecture Decision Register

## Records

| ID | Statement | Domain | Status | Evidence confidence | Record link |
|---|---|---|---|---|---|
| ADR-001 | Four repositories divide product, instance, infrastructure, and documentation authority. | Components/repositories | observed | High for source boundary; low for live ownership | [Record](adr/ADR-001-cross-repository-authority-boundary.md) |
| ADR-002 | Defaults, instance-owned configuration, and generated artifacts have separate ownership. | Configuration/artifacts | accepted | High for recorded source intent; runtime equivalence untested | [Record](adr/ADR-002-source-ownership-and-generated-artifacts.md) |
| ADR-003 | The redirector is a read-only Cloudflare Worker plus generated static assets/registry. | Runtime/data | observed | High for implementation; low for live deployment | [Record](adr/ADR-003-cloudflare-worker-runtime.md) |
| ADR-004 | Runtime validation and Cloudflare edge controls form separate protection layers. | Trust boundary | observed | High for source intent; low for applied effectiveness | [Record](adr/ADR-004-layered-edge-and-operational-access-controls.md) |
| ADR-005 | Review/check automation and human-signed tags form the declared release trust chain. | Release/delivery | accepted | High for declarations and sampled runs; unknown for settings/deployment | [Record](adr/ADR-005-release-and-delivery-trust-chain.md) |
| ADR-006 | Terraform describes demo edge controls while state/secrets remain external. | Infrastructure/configuration | observed | High for configuration; low for live ownership/state | [Record](adr/ADR-006-terraform-control-plane-and-external-state.md) |
| ADR-007 | Git is durable instance data and the runtime is a derived deployment. | Data/recovery | observed | High for implementation; recovery unexercised | [Record](adr/ADR-007-git-backed-instance-data-and-recovery-boundary.md) |

## Coverage And Disposition

| Domain | Candidates | Records | Other dispositions | Limitation |
|---|---:|---:|---|---|
| Components/repositories | 2 | 1 | 1 merged | Administrative control of each repository is unknown. |
| Configuration/data/artifacts | 3 | 2 | 1 merged | Build and restore were not executed. |
| Runtime/dependencies | 3 | 2 | 1 deferred to Product Value | Live topology, traffic, deployment, and analytics state are unknown. |
| Identity/trust/recovery | 2 | 2 | 1 candidate also merged across records | Actual account, policy, secret, and recovery ownership are unknown. |
| Capacity/cost/async | 2 | 0 | 1 blocked, 1 merged | No approved live workload, capacity, quota, SLO, or commercial evidence. |
