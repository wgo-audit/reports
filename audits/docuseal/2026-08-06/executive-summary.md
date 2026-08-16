# Executive Summary

## Mandate, Boundary, And Bottom Line

The organization is evaluating self-hosted DocuSeal Community as the eSignature foundation for all new-customer web/mobile onboarding within its existing SOC 2 control boundary. The assessed source is fixed at tag `3.1.7`, commit `a2d8b855491793870b7b4acf176d2d95ae95ff83`; the detailed mandate and exclusions are in the [audit brief](audit-brief.md).

**Recommendation: continue evaluation conditionally.** The pinned Community repository contains a substantive, inspectable multi-party signing core and a traceable release candidate. No reviewed evidence establishes a fatal absence that warrants stopping technical/vendor evaluation. Equally, no reviewed evidence supports production approval, an external legal/compliance/KYC claim, a customer commitment, or revenue-critical reliance.

The next stage should be a governed decision-and-proof program, not implementation by assumption. The organization must first decide the edition/integration, signing trust, customer workflow/readiness, signer assurance, workload, commercial, maintenance, claim, and release-authority boundaries. It must then prove the selected target through independent artifacts, supported web/mobile paths, controlled release, failure/recovery, capacity, access transfer, vendor terms, and consequence scenarios.

## Current Product And Control Position

The strongest positive evidence is concrete:

- Community `3.1.7` is a fixed, traceable source pin with an inspectable template-to-signing implementation, API/webhook mechanisms, signer events, result/audit generation, optional PDF signing/TSA paths, and verification logic ([E-001](evidence/evidence-ledger.md), [E-025–E-032](evidence/evidence-ledger.md)).
- All five configured upstream application CI jobs and the separate multi-architecture image-build/push job passed for the pinned release ([Code Quality](reviewer-reports/code-quality/report.md), [E-019](evidence/evidence-ledger.md)).
- The architecture, workflow, data, job, credential, provider, migration, and release surfaces are traceable enough to design exact target tests rather than rely on marketing claims ([Architecture](reviewer-reports/architecture/report.md)).
- Public project activity, source access, and visible release outputs support further diligence, while the audit correctly avoids converting Git labels into staffing, authority, knowledge, or bus-factor claims ([Contributor & Vendor Value](reviewer-reports/contributor-vendor-value/report.md)).

The production gap is also concrete:

- Required web/mobile integration crosses unresolved Community/Pro API, embed, identity, role, SAML, SMS, package, entitlement, and support boundaries ([OI-001](controls/open-items.md), [OI-005](controls/open-items.md), [OI-020](controls/open-items.md)).
- SQL completion precedes asynchronous evidence generation and downstream mail/webhook completion. The organization has not approved the authoritative readiness/revenue state or demonstrated reconciliation ([Product Value](reviewer-reports/product-value/report.md), [E-047](evidence/evidence-ledger.md)).
- Signature images, hashes, conditional PKI signing, optional TSA, generated audit snapshots, and verifier results are distinct mechanisms. No independent artifact suite, accepted trust model, immutable tenant-bound evidence, or specialist decision exists ([OI-002](controls/open-items.md), [OI-006](controls/open-items.md)).
- Community administration is broad; signer assurance and KYC binding are unresolved; source-visible authorization/session edge cases require focused testing; target secret/key custody and privacy lifecycle are unproved ([Security & Privacy](reviewer-reports/security-privacy/report.md)).
- Recovery must align SQL, blobs, keys, and queue state. The approved targets—99.5% monthly signing availability, 99% monthly onboarding availability, two-hour RPO, and permitted onboarding pause—are criteria, not achieved performance ([E-044](evidence/evidence-ledger.md), [Business Continuity](reviewer-reports/business-continuity/report.md)).
- The approved low/base/high scenario method supplies a valid capacity approach, but actual demand, latency, backlog, catch-up, retention, provider, and topology values remain unpopulated ([E-045](evidence/evidence-ledger.md), [OI-017](controls/open-items.md)).
- Public prices and terms are planning signals, not actual spend, a quote, an operative agreement, support, or commercial continuity. Total cost cannot be bounded before workload, topology, controls, staffing, rates, and terms are approved ([Expense Exposure](reviewer-reports/expense-exposure/report.md)).
- Upstream green jobs and a source tag do not create an organization-approved artifact or release. Release/change authority, exception rights, retained evidence, outcome observation, and learning are unproved ([Project Health](reviewer-reports/project-health/report.md), [OI-025](controls/open-items.md)).

## Material Risks, Unknowns, And Decisions

### Decision-Useful Conclusions

1. **Choose edition and maintenance posture before client binding or procurement.** Community exposes useful API/webhook mechanisms, while required embed/identity/role/package and support outcomes cross uninspected Pro/vendor boundaries. Decide [OI-001](controls/open-items.md) and [OI-021](controls/open-items.md), then obtain release-specific contract evidence through OI-005/OI-020.
2. **Define one authoritative onboarding-readiness state.** A relational completion timestamp is earlier than evidence and delivery readiness. Approve [OI-009](controls/open-items.md), then test crash, retry, backlog, consumer reconciliation, and artifact acceptance through OI-003/OI-006.
3. **Decide identity and signing trust before making assurance claims.** Email/link possession, SMS, KBA/ID methods, signature images, PKI signatures, timestamps, and KYC binding are not interchangeable. Decide [OI-002](controls/open-items.md), [OI-011](controls/open-items.md), and [OI-023](controls/open-items.md) before specialist testing or external claims.
4. **Promote an immutable, verified artifact—not a tag.** Upstream CI and image publication are separate, and no digest/SBOM/provenance/vulnerability/runtime acceptance gate binds reviewed source to deployment. Implement [OI-004](controls/open-items.md) under release authority [OI-025](controls/open-items.md).
5. **Use the allowed onboarding pause as safe-stop policy, not recovery evidence.** Safe pause can prevent unsafe continuation but does not reconcile accepted requests, queues, artifacts, consumers, or backlog. Implement [OI-014](controls/open-items.md) and prove OI-003/OI-006 against E-044's targets.
6. **Populate workload before capacity, cost, or business-consequence claims.** The approved scenario method does not supply values. Decide [OI-017](controls/open-items.md); only then execute capacity/recovery proof, total-cost modeling [OI-018](controls/open-items.md), and business-consequence scenarios [OI-024](controls/open-items.md).
7. **Treat visible activity as a diligence signal, not support or succession.** Git history and frequent tags do not establish authority, support performance, vendor health, or replacement capability. Close vendor commitments through OI-013/OI-020 and demonstrate organization ownership/transfer through OI-015/OI-016/OI-022.

### Decisions Now

- [OI-001](controls/open-items.md) — Community/Pro integration boundary.
- [OI-002](controls/open-items.md) — signing certificate, key custody, TSA, and verification trust model.
- [OI-009](controls/open-items.md) — customer-facing signing contract and authoritative readiness state.
- [OI-011](controls/open-items.md) — signer identity-assurance tiers and KYC/jurisdiction sufficiency route.
- [OI-013](controls/open-items.md) — vendor security-maintenance commitment.
- [OI-017](controls/open-items.md) — bounded low/base/high workload and SLO envelope.
- [OI-019](controls/open-items.md) — budget, billing, renewal, quota, dispute, escalation, and fallback authority.
- [OI-021](controls/open-items.md) — minimal Community, maintained fork, vendor-supported Pro, or replacement maintenance posture.
- [OI-023](controls/open-items.md) — claim/evidence/authority/expiry governance.
- [OI-025](controls/open-items.md) — organization release/change authority and traceability.

### Evidence Needed

- [OI-003](controls/open-items.md) — target topology, ingress/egress, capacity, dependency readiness, failure, recovery, observability, and controlled-resume proof.
- [OI-005](controls/open-items.md) — release/edition-specific API, webhook, embed, package, compatibility, retry, and support/deprecation evidence.
- [OI-006](controls/open-items.md) — independent artifact, trust, integrity, lifecycle, cross-store restore, crash/replay, and specialist acceptance evidence.
- [OI-007](controls/open-items.md) — reproducible local gate outcomes and measured coverage.
- [OI-010](controls/open-items.md) — approved web/iOS/Android golden paths and material failures.
- [OI-016](controls/open-items.md) — emergency access, privileged replacement, credential/key rotation, and control transfer.
- [OI-018](controls/open-items.md) — target total-cost model using approved quantities and rates.
- [OI-020](controls/open-items.md) — release-specific Pro quote and operative agreement.
- [OI-022](controls/open-items.md) — replacement-maintainer product safe-change exercise.
- [OI-024](controls/open-items.md) — populated and exercised business-consequence scenarios.

### Implementation Corrections

- [OI-004](controls/open-items.md) — controlled artifact intake, vulnerability assessment, migration, promotion, upgrade, and rollback.
- [OI-008](controls/open-items.md) — Vue, mobile/webview, accessibility, and release-delta gates.
- [OI-012](controls/open-items.md) — focused authorization/session negative tests and remediation of confirmed gaps.
- [OI-014](controls/open-items.md) — availability measurement, readiness, monitoring, incident command, safe pause, communication, reconciliation, and controlled resume.
- [OI-015](controls/open-items.md) — service/account/source/vendor inventory with two trained maintainers, backup owners, and knowledge-transfer evidence.

## Evidence-Supported 30–90 Day Plan

| Timing | Accountable owner | Action | Evidence basis | Exit evidence |
|---|---|---|---|---|
| Days 0–15 | CEO, Product Manager, VP Software Engineering, CISO | Decide edition/integration and maintenance posture; appoint release/change and commercial authorities | OI-001/OI-019/OI-021/OI-025; [E-060](evidence/evidence-ledger.md) | Approved versioned decision records, owner matrix, stop conditions, and vendor-evidence request |
| Days 0–30 | Product Manager, CISO, legal/compliance authority | Approve customer workflow/readiness, identity-assurance tiers, signing trust, and claim-governance boundaries | OI-002/OI-009/OI-011/OI-023; [Product Value](reviewer-reports/product-value/report.md) | Approved acceptance oracles, prohibited claims, specialist questions, and evidence expiry rules |
| Days 15–30 | Product Manager, IT Operations Director, VP Software Engineering | Populate low/base/high workload/SLO scenarios and select one target topology candidate | OI-017/OI-003; [Scalability](reviewer-reports/scalability/report.md) | Versioned workload envelope and target architecture/provider diagram with quotas and measurement points |
| Days 15–45 | IT Operations Director, VP Software Engineering, CISO | Build immutable artifact, vulnerability, migration, promotion, rollback, and change-record gates | OI-004/OI-025; [E-040–E-041](evidence/evidence-ledger.md) | Digest-bound candidate, SBOM/provenance/scans, migration/backup evidence, approval and rollback record |
| Days 30–60 | Product Manager, VP Software Engineering, CISO | Run supported web/mobile golden paths, authorization negatives, target frontend gates, and independent artifact known-answer tests | OI-006/OI-008/OI-010/OI-012 | Retained pass/fail evidence, signed/unsigned/tampered fixtures, consumer results, and classified/remediated security findings |
| Days 30–60 | IT Operations Director, Product Manager, VP Software Engineering | Implement service indicators, dependency readiness, alerts, incident roles, safe pause, communication, and resume criteria | OI-014/OI-015; [Business Continuity](reviewer-reports/business-continuity/report.md) | Alert-delivery proof, monthly measurement definition, owner inventory, incident exercise, and controlled-resume record |
| Days 45–75 | IT Operations Director, VP Software Engineering, CISO | Exercise capacity, queue/backlog, failure, cross-store restore, reconciliation, access transfer, and replacement-maintainer safe change | OI-003/OI-006/OI-016/OI-022 | Results against approved scenarios/RPO, reconciled artifacts/consumers, transfer record, and successor-produced release evidence |
| Days 60–90 | CEO, Product Manager, finance/procurement, IT Operations Director | Reconcile vendor support/terms, total cost, and business-consequence scenarios; make the next-stage decision | OI-005/OI-013/OI-018/OI-020/OI-024 | Approved vendor matrix/agreement, cost ranges, exercised consequence scenarios, residual-risk decision, and explicit continue/stop/production-test authorization |

## Reader Routing And Limits

Product capability and promise boundaries are in [Product Manager Notes](product-manager-notes.md). Architecture, quality, security, operations, and safe-evolution detail is in [Technical Lead Notes](technical-lead-notes.md). Direct evidence remains authoritative; reviewer handoffs and these reports are navigation and reconciliation aids.

The [API-equivalent cost estimate](controls/cost-estimate.md) is **Unreconciled**: two auditor-authorized Terra passes exactly reconcile a USD 151.4883488 subtotal for 28 included sessions, but one collector lacks the terminal lifecycle cutoff required for a complete audit total. It is not a Codex invoice.

No local product gates, penetration test, load test, live deployment, restore, incident, target golden path, Pro implementation review, contract review, or legal/compliance determination was performed. Coverage is unmeasured, and public list prices/terms are not commitments.

Structural validation not run: the canonical validator is absent from the active audit root.
