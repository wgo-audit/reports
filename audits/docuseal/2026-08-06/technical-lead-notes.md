# Technical Lead Notes

## Current Technical Position

The assessed DocuSeal Community `3.1.7` source is a traceable Rails modular monolith with ERB/Turbo/Vue UI, SQL workflow state, Active Storage blobs, Redis/Sidekiq jobs, API/webhooks/mail, PDF/audit generation, optional PKCS/TSA signing, container delivery, and configurable SQL/blob/Redis/provider boundaries. It is technically intelligible enough to design exact target validation ([Architecture](reviewer-reports/architecture/report.md)).

The upstream baseline is useful but bounded: five configured application jobs and the tag image-build/push job passed. Local reproduction did not run because the approved host lacked the locked toolchain/dependencies and installation was not authorized. Coverage and exact RSpec outcomes remain unmeasured. Upstream tag/image status does not identify an accepted or deployed digest ([Code Quality](reviewer-reports/code-quality/report.md)).

## Architecture, Operations, Quality, And Security Findings

- **Edition/contracts:** Community implements some API/webhook behavior, while OpenAPI/embed/identity/role/package and support boundaries differ across Community, Pro, public documentation, and external components. OI-001/OI-005 own the selected release contract.
- **Completion topology:** relational completion precedes Sidekiq/Redis finalization, blobs, mail, and webhooks. No transactional outbox or demonstrated end-to-end reconciliation exists. OI-009 must define readiness; OI-003/OI-006 must prove crash/replay/backlog/consumer behavior.
- **Data/recovery:** SQL, blobs/provider metadata, keys/secrets, and queue state form one recovery set. Independent database and bucket recovery is insufficient. Prove time alignment, key usability, queue/schedule recovery, artifact integrity, and downstream reconciliation against the two-hour RPO.
- **Migrations/releases:** production can run migrations at boot; the pinned set includes non-reversible/model-coupled work. Separate migration authority from application startup and require backup, compatibility, rollback/roll-forward, and post-change recovery evidence.
- **Artifact provenance:** CI and image publication are separate workflows. Build and promote a digest-bound artifact through SBOM, dependency/image/secret scans, provenance/signature, policy/exception, runtime-smoke, migration, backup, and rollback gates under OI-004/OI-025.
- **Quality:** the source suite is broad, but target-required Vue/mobile/webview/accessibility, independent artifact/contract, upgrade, failure/recovery, and immutable-promotion gates remain open. Execute OI-007/OI-008/OI-010 without converting static example declarations into coverage.
- **Identity/access:** Community has broad administrators, long remembered sessions by default, optional/per-user MFA behavior, broad bearer API tokens, capability-link signers, and a source-visible attachment-authorization mismatch requiring safe negative tests. Do not infer exploitability; close OI-012 and design the target IAM/session/service-identity boundary in OI-003.
- **Secrets/trust:** a shared root can serve multiple encryption/token/session purposes; PKCS#12 bytes and password share an encrypted record. OI-002 must define independent custody, rotation, revocation, recovery, certificate/TSA trust, and verifier acceptance before artifact testing.
- **PII lifecycle:** identity/signing data spans SQL, blobs, events, search/text derivatives, generated artifacts, and optional webhooks. Archive differs from destroy. OI-006 must prove retention, legal hold, derivative cleanup, backup erasure, and restore integrity.
- **Ingress/egress:** example Compose publishes Caddy and Rails, SSL is conditional, privileged/public routes share a listener, controls are route-local, and remote destinations have differing validation. OI-003 must prove listener/firewall/WAF/TLS/header/proxy/abuse/SSRF/egress policy against the actual topology.
- **Capacity/observability:** source concurrency knobs, retries, timeouts, `/up`, logs, and public sizing are hypotheses, not capacity/readiness proof. Populate OI-017, then test saturation, pools, provider quotas, queue drain, backlog, dependency readiness, and customer-visible indicators through OI-003/OI-014.
- **Ownership/change:** visible tags and Git activity do not establish release authority, vendor support, or successor capability. OI-015/OI-016/OI-022/OI-025 establish two maintainers, control transfer, safe-change performance, and retained release decisions.

## Safe Evolution Priorities

1. **Freeze the decision boundary:** approve OI-001/OI-002/OI-009/OI-011/OI-017/OI-021/OI-025 before target implementation diverges.
2. **Select one target topology:** document ingress, runtime replicas, workers/Redis, SQL, blobs, secrets/KMS/HSM, signing/TSA, SMTP/webhook consumers, monitoring, backup, and provider quotas under OI-003.
3. **Create one immutable candidate lane:** use OI-004 to bind source, dependencies, image digest, scans, SBOM/provenance, migration, backup, promotion, rollback, and post-change verification to one OI-025 change record.
4. **Build independent acceptance:** OI-006/OI-008/OI-010/OI-012 should cover known-answer signed/unsigned/tampered artifacts, web/mobile/accessibility, release/edition consumers, authorization negatives, migration, crash/retry/reconciliation, and restore.
5. **Instrument service and safe pause:** OI-014 defines customer-visible availability denominators, dependency readiness, evidence-readiness indicators, alerts, incident command, communication, reconciliation, and controlled resume.
6. **Exercise before costing:** prove approved low/base/high scenarios, recovery, transfer, and replacement-maintainer behavior through OI-003/OI-006/OI-016/OI-022; only then populate OI-018/OI-024.
7. **Retain vendor and specialist evidence:** OI-005/OI-013/OI-020 must bind release-specific entitlement, supported versions, security response, packages, support, commercial continuity, transition, and exit.

## Traceability And Limits

Use the [evidence ledger](evidence/evidence-ledger.md) for canonical facts and limitations, [open items](controls/open-items.md) for owner/closure routes, [Architecture ADR register](controls/architecture/adr-register.md) for source-bounded technical decisions, [Security trust diagram](controls/security/diagrams/identity-data-trust-boundaries.md), [Continuity recovery control](controls/continuity/recovery-and-service-control.md), [Scalability envelope](controls/scalability/capacity-envelope.md), [Maintenance time-to-safety](controls/maintenance/time-to-safety.md), and [Project Health release/change control](controls/project-health/release-change-control.md).

The [API-equivalent cost estimate](controls/cost-estimate.md) is **Unreconciled**: two auditor-authorized Terra passes produce byte-identical request-level evidence and a USD 151.4883488 subtotal for 28 included sessions, but one collector lacks the terminal lifecycle cutoff required for a complete audit total. It is not a Codex invoice.

No dependency installation, local product suite, penetration test, load test, live topology inspection, deployment, migration, restore, incident, key rotation, or code remediation ran. Pro implementation, external packages, registry state, private review, operative contracts, and specialist determinations remain outside the evidence boundary. Source mechanisms do not prove live effectiveness, capacity, correctness, security, ownership, cost, or readiness.

Structural validation not run: the canonical validator is absent from the active audit root.
