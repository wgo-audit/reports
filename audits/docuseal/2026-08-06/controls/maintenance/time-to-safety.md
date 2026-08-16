# Maintenance Time-To-Safety And Ownership Boundary

Coordinator mapping: local MC-OI-001/002 are serialized as canonical OI-021/OI-022. Local labels remain below for traceability to the reviewer draft.

## Reader Question And Boundary

What must a replacement team be able to reproduce, understand, verify, operate, and transfer before a change to DocuSeal can be called safe for regulated onboarding?

This is an evidence-gate map, **not an elapsed-time, staffing, productivity, or cost estimate**. It uses pinned source/history, the [maintenance evidence packet](../../evidence/packets/maintenance-cost-work-surfaces.md), and completed predecessor controls. No organization skill inventory, staffing plan, time study, target environment, operator exercise, vendor commitment, or financial evidence was supplied.

## Safe-Change Evidence Sequence

| Gate | Confirmed starting point | Evidence required before the gate is satisfied | Current state and route |
|---|---|---|---|
| 1. Establish what is owned | Pinned Community source; some API/webhook behavior; known external/Pro boundaries | Approved minimal-Community, maintained-fork, vendor-supported-Pro, or replacement posture, including upstream intake/freeze and exit | **Open.** Proposed MC-OI-001; edition/contracts/support/commercial proof remains OI-001/OI-005/OI-013/OI-020. |
| 2. Reproduce the candidate | Lockfiles, Dockerfile, CI workflows, passed hosted jobs | Approved immutable source/artifact, reproducible toolchain, dependency/native-input verification, SBOM/provenance/scans, retained exact gate results | **Open.** OI-004/OI-007; configured hosted jobs are only a starting signal. |
| 3. Bound the change | Traceable Rails/UI/API/jobs/data/artifact/runtime surfaces and frequent-path history | Change-to-contract/data/job/artifact/provider impact classification; named reviewer/owner; edition/release compatibility | **Open.** OI-005/OI-009/OI-015 plus the hotspot table below. |
| 4. Prove mandate-critical behavior | RSpec/system/request/job tests and source-visible hashes/signatures/retries | Independent signed/audit known answers; web/mobile/accessibility; consumer contracts; migration/failure/recovery; authorization/security regressions | **Open.** OI-006/OI-008/OI-010/OI-012. |
| 5. Prove target operation | Configurable runtime/stores/queues/providers and approved availability/RPO/scenario method | Populated OI-017 oracle; target capacity/readiness/observability; safe pause, alert, recovery, backlog/reconcile/resume evidence | **Open.** OI-003/OI-014/OI-017. |
| 6. Promote and recover | Tag image job and boot-coupled migration behavior | Digest-bound promotion, dedicated migration, compatibility, backup, rollback/roll-forward, post-change verification and recovery evidence | **Open.** OI-004/OI-006. |
| 7. Transfer safely | Identifiable application/provider/account/key control surfaces | Primary/backup owners; emergency access; replacement-admin/key rotation; replacement maintainer performs the full product safe-change sequence with retained evidence | **Open.** OI-015/OI-016 plus proposed MC-OI-002, or an explicit expansion of OI-016's closure route. |

No stage has a supported elapsed duration. A green upstream job does not bypass the remaining gates.

## Skill And Operating-Surface Map

| Work surface | Source-visible technology/obligation | Why it is safety-relevant | Evidence limit |
|---|---|---|---|
| Application and domain | Ruby 4.0.5, Rails, models/controllers/services, RSpec | Workflow state, authorization, lifecycle, contracts, migration behavior | No target maintainer or demonstrated successor. |
| Browser and target channels | ERB, Turbo, Vue, Webpack, signer/builder bridges | All-new-customer web/mobile onboarding and accessibility compatibility | External embed packages and target mobile hosts outside scope; current gate gaps under OI-008/OI-010. |
| Documents and evidentiary artifacts | PDFium, HexaPDF, VIPS, fonts, signatures, hashes, PKCS#12, TSA | Result/audit correctness, tamper evidence, verification and specialist acceptance | No independent artifact suite or accepted trust model. |
| Data, jobs, and integrations | PostgreSQL/SQLite/MySQL, Active Storage, Redis/Sidekiq, mail, webhook/API | Atomicity boundaries, retries, reconciliation, retention, migration and recovery | No target topology, failure exercise, retention or consumer contract proof. |
| Platform and release | Alpine container, native libraries, multi-arch build, GitHub Actions, migration-at-boot option | Reproducibility, vulnerability intake, promotion, rollback and runtime compatibility | No approved target artifact, SBOM/provenance, release lane or rollback exercise. |
| Security, privacy, and operations | IAM/session/token/key lifecycle, ingress/egress, PII stores, monitoring, incident, recovery | Sensitive KYC data, availability/RPO, response and successor safety | No assigned primary/backup owners, effective control evidence, or transfer rehearsal. |
| Vendor/legal/commercial boundary | Community/Pro, external packages, AGPL/additional term, public terms | Determines which work/risks are owned, bought, supported, or replaceable | Pro code, executed agreement, support commitments and legal determination unavailable. |

The table shows domains a maintenance plan must cover. It does not prescribe headcount or require one person per row.

## Change-Frequency And Coupling Review Priorities

| Priority surface | Cutoff-bounded signal | Required review emphasis | Prohibited inference |
|---|---|---|---|
| Template builder and signer form | Repeatedly changed Vue/form files; `3.1.7` was frontend-heavy | Target web/mobile/accessibility and payload compatibility | Frequency is not defect rate or UI quality. |
| Completion, result, and audit generation | Repeated changes in result/audit/submit paths; workflow crosses SQL, queue, blobs, signing, mail/webhook | Independent artifacts, crash/retry/reconcile, readiness semantics | Coupling is not observed failure or repair time. |
| Routes/API/edition contracts | Routes and API submission code recur in history; source/public/Pro contract boundaries differ | Release/edition-specific consumer contract and authorization checks | Source presence is not entitlement or compatibility. |
| Dockerfile, lockfiles, schema/migrations | Repeated changes overlap build/native inputs and data compatibility | Immutable intake, scans, representative upgrades, backup and rollback/roll-forward | Change count is not supply-chain compromise or migration failure. |

Exact method and limits are in MC-E-004. These are review-prioritization signals, not quantified complexity scores.

## Replace-Versus-Own Decision Boundary

| Path | Organization must own regardless | Additional evidence before selection | Maintenance conclusion supported now |
|---|---|---|---|
| Community, minimal/no fork | Target deployment, security controls, recovery, monitoring, release intake, data lifecycle, integration adapter, acceptance evidence, incident/account ownership | Legal interpretation, supported-version/security-response evidence, target capability fit | Inspectable base; safe recurring ownership remains substantial and unquantified. |
| Community with maintained modifications | Everything above plus fork merge/rebase, divergence, regression, source-release, and replacement knowledge | Approved modification policy, upstream contribution/fork strategy, legal determination, successor proof | No approved fork posture or safe-change exercise exists. |
| Pro/self-hosted vendor-supported path | Target operations/control boundary and organization acceptance evidence remain owned | Release-specific entitlement/code-interface evidence, support/security/upgrade commitments, operative terms, external package lifecycle, exit rights | May transfer some implementation/support work, but unavailable Pro/contract evidence prevents a maintenance claim. |
| Replace DocuSeal | Target requirements, data/evidence migration, customer-channel compatibility, security/recovery, legal/compliance acceptance | Alternative evidence, migration/exit design, retained verification and continuity plan | No alternative product or replacement lead-time evidence was approved; no comparative conclusion is available. |

## Diagram

The [safe-change and ownership diagram](diagrams/safe-change-and-ownership-boundary.md) shows the source-visible upstream intake and the unproved target gates without implying duration.

## Open Routes And Cost Boundary

Proposed `MC-OI-001` should ask the authorities to choose minimal Community, a maintained Community fork, vendor-supported Pro, or replacement, including intake/freeze and exit posture. Edition contracts, release controls, vendor support and commercial proof remain with OI-001/OI-004/OI-005/OI-013/OI-020.

Proposed `MC-OI-002` should verify that a replacement maintainer can reproduce, change, test, promote and rollback/recover the product in non-production. This is distinct from OI-016's current administrative/key/control-transfer scope; the coordinator may instead expand OI-016 explicitly to include the full product exercise. The proof reuses OI-004/OI-006/OI-007/OI-008/OI-014/OI-015/OI-016.

OI-017 owns the approved workload/SLO quantities. OI-018 owns the later maintenance and total-cost model using approved topology, workload, control scope, skill availability, staffing quantities, specialist/vendor commitments, and organization rates. This control supplies work surfaces only and supports no hours, staffing, or money.
