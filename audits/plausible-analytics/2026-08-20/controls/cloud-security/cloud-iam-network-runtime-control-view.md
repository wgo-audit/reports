# Cloud, IAM, Network, And Runtime Control View

## Evidence Boundary

Reader question: Which cloud-adjacent controls are visible in approved source, and what must be proved before Run or Subscribe can be treated as effectively isolated?

The view uses [E-003](../../evidence/evidence-ledger.md#e-003), [E-026](../../evidence/evidence-ledger.md#e-026), [E-030](../../evidence/evidence-ledger.md#e-030), [E-035](../../evidence/evidence-ledger.md#e-035), [E-040](../../evidence/evidence-ledger.md#e-040), and [E-041](../../evidence/evidence-ledger.md#e-041). No library or hosted cloud account, IAM, DNS, TLS, WAF, registry, secret store, runtime, traffic, or contract was accessed. Source presence and public statements do not prove effective controls.

## Evidence Dimensions Used

Implementation and configuration mechanisms are present. Current hosted security statements are post-cutoff public assertions only. Live operation, ownership/approval, cost, and independent specialist/assurance evidence are unknown.

## Current Source-Bounded Position

| Boundary | Source-visible position | Effective status | Material limit and closure |
|---|---|---|---|
| Cloud account and IAM | Application roles and secret consumers exist, but no infrastructure account/project, workload identity, admin role, break-glass route, or IAM policy is in the approved corpus. | unknown | Inventory option-specific identities, least privilege, MFA, logging, successor access, and separation through [OI-001](../open-items.md#oi-001) and [OI-015](../open-items.md#oi-015). |
| Public ingress and client identity | The image listens on `0.0.0.0:8000`; the application accepts the first supported forwarding/classification header without a source-visible trusted-proxy allowlist. | unknown; acceptance-blocking | Prove that the selected edge overwrites privileged headers and enforces hostname/rate/domain controls with synthetic non-production attempts through [OI-011](../open-items.md#oi-011). Do not infer exposure from the listening socket alone. |
| TLS and network segmentation | CE can terminate TLS 1.2/1.3 when configured. PostgreSQL transport otherwise defaults to no TLS and ClickHouse to HTTP, based on an explicit co-location assumption. | unknown | Map termination, certificate ownership/renewal, private routes/firewalls, datastore TLS verification, credentials, and egress through [OI-001](../open-items.md#oi-001). Plaintext defaults are acceptable only inside a verified boundary. |
| Container runtime | Final image runs as uid 999 and application files are copied mode 555. The persistent volume path is writable by all container users; root filesystem, capabilities, seccomp, resource limits, volume sharing, and admission policy are not source-defined. | partial mechanism; effectiveness unknown | Verify the deployed security context, read-only root, dropped capabilities, volume ownership/mode, isolation, and resource policy through [OI-001](../open-items.md#oi-001). |
| Secrets | Runtime prefers mounted files under `/run/secrets` and validates selected key shape/length; environment values remain supported. | partial mechanism; custody unknown | Record redacted secret provider, identities/ACLs, injection path, rotation and fallback-key removal, and diagnostic/export destinations through [OI-001](../open-items.md#oi-001). Preserve governance under [OI-008](../open-items.md#oi-008). |
| Datastore roles and pools | Separate ClickHouse repositories encode read-only queries, ingest, asynchronous insert, and deletion roles; several pool and timeout values are explicit/configurable. | source-separated; credential enforcement unknown | Verify distinct principals/permissions, TLS, network paths, pool sizing, and queue behavior. Do not treat separate clients as proof of separate credentials or least privilege ([OI-001](../open-items.md#oi-001)). |
| Health and telemetry | Liveness is unconditional; readiness checks PostgreSQL, ClickHouse, critical caches, and session-transfer attempt. PromEx is disabled by default and OpenTelemetry/BEAM export is conditional. | mechanisms present; wiring/alerts unknown | Verify external probe use, protected metrics access, alert rules/owners, queue/buffer/deletion/report signals, and failure drills through [OI-001](../open-items.md#oi-001), [OI-003](../open-items.md#oi-003), and [OI-014](../open-items.md#oi-014). |
| Hosted Subscribe controls | Current public material claims encryption, RBAC/MFA/zero-trust access, monitoring, scanning, and backups. | public assertion only | Treat [E-030](../../evidence/evidence-ledger.md#e-030) as post-cutoff validation. Procurement/security review must obtain dated, service-specific IAM, network, runtime, supply-chain, monitoring, deletion, and recovery evidence plus responsibility terms through [OI-015](../open-items.md#oi-015). |

## Material Unknowns And Closure Routes

Run cannot be accepted from source defaults alone: [OI-001](../open-items.md#oi-001) establishes the redacted effective control inventory, [OI-011](../open-items.md#oi-011) proves the edge boundary, and [OI-005](../open-items.md#oi-005) binds the deployed digest. Subscribe transfers infrastructure operation but still requires option-specific assurance and named library account/data responsibilities through [OI-015](../open-items.md#oi-015). Replace has no approved candidate and receives no security credit from absence of evidence.
