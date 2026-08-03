# Business Continuity

## Audit Question, Depth, And Evidence Boundary

This detailed review asks whether vanityURLs can be demonstrated, changed, deployed, operated, detected, recovered, and transferred if creators, maintainers, accounts, vendors, or environments disappear. It directly addresses sudden creator departure or shifting interest and the harmful failure defined in the brief. Evidence is public and cutoff-pinned through July 22, 2026: four repositories/history, documentation, hosted metadata, recovery/operations and ownership packets, and prior reviewer handoffs. No authenticated inventory, private handover, live runtime, alert, billing, registrar, state, credential, deployment, rollback, restore, or successor drill was approved.

## Coverage And Material Gaps

Coverage includes source/data portability, maintainer/repository control, releases/signers, domain/DNS/Cloudflare, Terraform state, secrets, deployment, logs/alerts, incidents, rollback/recovery, renewals, and non-creator onboarding. Public evidence strongly supports software reconstruction and independent forking. It does not support control transfer for the existing canonical project, domain, or demo service. The material missing evidence is consolidated in OI-001 through OI-007, OI-010, and OI-012 rather than silently treated as private-but-present.

## Key Findings

| Finding | Evidence links | Confidence and limitation | Consequence |
|---|---|---|---|
| Core software and link data are portable: public MIT source, Git history, tests, ADRs, releases, detached-instance design, and broad operator docs reduce creator knowledge dependency. | [Continuity matrix](../../controls/continuity/continuity-and-transfer-matrix.md), [Architecture report](../architecture/report.md), [Product report](../product-value/report.md) | High for public artifacts; successor execution unobserved. | If creators abandon the project, someone else can fork and continue technical evolution with moderate effort. |
| Canonical-project takeover is not transfer-ready: GitHub ownership/admin/rules, release signer recovery, maintainer appointment, and cross-repository authority are unknown. | [Vendor packet](../../evidence/packets/vendor-ownership-commercial.md), [E-003/E-013](../../evidence/evidence-ledger.md), OI-001/OI-002 | High for missing public proof; private arrangements may exist. | A new maintainer cannot be expected to onboard with minimal creator involvement or preserve canonical trust. |
| Existing-service operation is not transfer-ready: domain/renewal, Cloudflare owners/admins/secrets, Terraform state/import/drift, deployment connection, and live artifact are unproved. | [Continuity matrix](../../controls/continuity/continuity-and-transfer-matrix.md), [ADR-006](../../controls/architecture/adr/ADR-006-terraform-control-plane-and-external-state.md), [E-016](../../evidence/evidence-ledger.md) | High for public evidence gap; no authenticated source allowed. | A third party may build a new instance, but cannot be trusted to operate or recover the existing `v8s.link` service after sudden departure. |
| Rollback instructions and Git recovery concepts exist, but no backup/restore runbook, Terraform backend/state recovery, RTO/RPO, failover, or exercised recovery result exists publicly. | [Recovery packet](../../evidence/packets/recovery-and-operations.md), [observability path](../../controls/business-continuity/diagrams/observability-and-response-path.md) | High for source/document search; private recovery material unknown. | “Recoverable” cannot be claimed, and a successor has no evidence-based stop/escalation path. |
| Invocation logs and public intake are declared, but alert delivery, monitored contacts, on-call ownership, severity/escalation, communications, and incident records are absent. | [E-015](../../evidence/evidence-ledger.md), [observability path](../../controls/business-continuity/diagrams/observability-and-response-path.md) | High for declarations/gaps; live/private operations unknown. | A harmful outage or abuse event may go undetected or unowned, creating the community-distrust scenario in the brief. |
| Operational and documentation repositories concentrate work and lack equivalent governance/change controls. | [Project Health report](../project-health/report.md), [E-010](../../evidence/evidence-ledger.md) | High for public history; contribution value/availability not inferred. | Sudden departure affects the least reviewed components most severely. |

### Decision Insights

- **Current answer: no for low-touch canonical maintainer onboarding and no for third-party operation of the existing service.** Public forkability does not transfer external authority. The smallest decision/action sequence is OI-001, then OI-002/OI-006, then OI-003/OI-004.
- **A clean-room independent instance is the safest first continuity proof.** It avoids changing the existing service while testing whether documentation/source are sufficient. Success would prove fork operability, not canonical takeover; those acceptance criteria must stay separate.
- **Treat domain renewal and alert delivery as P1 continuity controls.** Code recovery cannot restore community trust if the public domain expires or failures are not noticed. Smallest actions: include renewal custody in OI-002 and implement OI-012.
- **Do not write runbooks before authority and scope are approved.** Procedures without owners/access would create false confidence. The later operationalization stage should draft aids only after synthesis approval and must keep them `draft`/untested until OI-004/OI-006 exercises.

## Selected Outputs

- Triggered [continuity and transfer matrix](../../controls/continuity/continuity-and-transfer-matrix.md), including direct answers for fork, maintainer takeover, independent instance, and existing-service operation.
- Triggered [observability and response path](../../controls/business-continuity/diagrams/observability-and-response-path.md), using approved logging/intake/rollback declarations while marking alert, owner, and recovery handoffs unknown.

The ephemeral artifact-quality review kept the matrix and flow separate because transfer readiness and incident response are different reader decisions. The artifacts were revised to state “portable” versus “transferable” explicitly and to prevent documented rollback from being read as tested recovery.

## Material Omissions, Unknowns, And Stakeholder Questions

- Continuity scope and community promise: OI-001.
- Actual owners, administrators, signers, recovery factors, domain renewal, payment ownership, successor authority: OI-002.
- Redacted handover/offboarding/recovery/incident procedure: OI-003 after approval.
- Independent successor setup/change/release/deploy/rollback/recovery evidence: OI-004.
- Applied infrastructure, state/import/drift, deployment, logs/alerts, last-known-good artifact: OI-006.
- Operational-repository review/CI: OI-007.
- Signed-upgrade authenticity: OI-010.
- Alert delivery, two-person response, monitored contacts, and incident evidence: OI-012.

## Reconciliation

Broad public documentation and a detailed release/rollback workflow were reconciled with missing exercised proof: they make reconstruction easier but do not establish recovery. Two declared product maintainers and two release signers were reconciled with single-person website governance and highly concentrated histories: declarations reduce single-person design intent but do not prove redundant access or availability. Terraform “source of truth” was reconciled as intended configuration authority, not recoverable live state.

## Bounded Conclusion And Downstream Guidance

Someone can plausibly fork vanityURLs and pursue its evolution after abandonment because the code, design history, tests, and documentation are public and substantial. The project cannot currently be described as easy for a new canonical maintainer to inherit with minimal creator involvement, nor can a third party be trusted to operate the existing project/domain/demo. The missing elements are authority, custody, transfer, alerting, recovery, renewal, and exercised proof—not a wholesale code rewrite. Wave 3 reviewers may use these conclusions for burden, concentration, cost, and risk; they must not infer actual owner unavailability, outage, spend, or private-document absence.
