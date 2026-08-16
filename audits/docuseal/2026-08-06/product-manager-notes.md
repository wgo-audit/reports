# Product Manager Notes

## Capability, Workflow, And Promise Position

DocuSeal Community `3.1.7` contains a substantive, inspectable signing foundation: templates, ordered/parallel signers, required fields, signature images, attachments, signer events, result/audit generation, downloads, API/webhook mechanisms, optional email OTP, hashes, conditional PDF signing/TSA, and verifier paths are present ([Product Value](reviewer-reports/product-value/report.md)). This is enough to continue product evaluation; it is not evidence that the organization's web/iOS/Android onboarding is ready.

The most important workflow distinction is **submission completion versus evidence readiness**. Signer completion commits relational state and then separately schedules artifact, email, and webhook work. The organization must decide which state authorizes customer activation or another commercial event under [OI-009](controls/open-items.md), then prove failure/retry/backlog/reconciliation behavior.

Product language must remain narrower than vendor positioning:

- A signature image or completion event does not prove disclosure, consent, intent, identity, enforceability, or legal effect.
- Email OTP or link possession is not a KYC identity-binding decision.
- Generic file/image attachment intake is not a verified KYC-document pipeline.
- A hash match, conditional PDF signature, optional timestamp, generated audit PDF, and tenant-bound immutable evidence are different outcomes.
- Public legal/compliance/KYC/verification language is not an organization-approved claim for this Community target.

The required integration remains an edition decision. Community contains some API/webhook behavior, while embedding, advanced identity, granular roles, SAML, external packages, entitlement, compatibility, and support cross uninspected Pro/vendor boundaries. Do not freeze the target client contract until OI-001/OI-005/OI-020 close with release-specific evidence.

## Decisions And Specialist Sign-Off Boundaries

Product Manager decisions requiring coordinated authority:

- [OI-001](controls/open-items.md): select Community/Pro and the exact web/mobile integration boundary.
- [OI-009](controls/open-items.md): approve actors, order, signature modality, disclosure/consent/intent evidence, partial-document behavior, authoritative readiness, outputs, and exceptions.
- [OI-011](controls/open-items.md): map transaction classes to signer-assurance tiers and fallback.
- [OI-017](controls/open-items.md): approve low/base/high demand, file/signer/page, latency, backlog, catch-up, and retention scenarios with Engineering and Operations.
- [OI-021](controls/open-items.md): choose minimal Community, maintained fork, vendor-supported Pro, or replacement posture.
- [OI-023](controls/open-items.md): approve exact claim wording, evidence, authority, prohibited implications, and expiry.
- [OI-025](controls/open-items.md): define how Product participates in priority, acceptance, exception, release, and learning decisions.

Required specialist boundaries remain outside this audit:

- Legal/compliance: jurisdictional eSignature validity/enforceability; disclosure/consent/intent; AGPL/additional-attribution application; customer contract/SLA/remedy language.
- CISO/legal/compliance: KYC identity-binding sufficiency, accepted assurance tiers, signature trust, TSA/certificate model, evidence integrity, privacy/data-residency/retention decisions.
- DocuSeal vendor: release-specific Pro entitlement, packages, contracts, support/deprecation, supported versions, security response, metering, renewal, transition, and exit.

No source or public statement should be presented as one of these determinations.

## Material Gaps, Risks, And Next Work

1. **Target golden path:** execute [OI-010](controls/open-items.md) for approved web/iOS/Android actors using safe identity/KYC/artifact fixtures. Include disclosure, identity challenges, ordered/parallel signers, retries, partial/completed downloads, audit, webhook, altered artifacts, and supported upgrades.
2. **Readiness and recovery:** bind the Product readiness state to OI-003/OI-006/OI-014 so pause, recovery, backlog, reconciliation, and controlled resume cannot create an accepted-looking incomplete onboarding.
3. **Edition contract:** obtain OI-005/OI-020 evidence before client implementation or procurement commitment.
4. **Claims and demo:** use [Revenue Claim Governance](controls/revenue/claim-governance.md) and [Demo Readiness](controls/revenue/demo-readiness.md). A vendor demo link or source path is not an organization-approved demo.
5. **Business consequences:** populate [OI-024](controls/open-items.md) only after OI-017 supplies workload/SLO values and OI-009/OI-014 define readiness and interruption measurement. Do not invent revenue or loss inputs.
6. **Commercial comparison:** compare Community and Pro only after assurance choices, completion volumes, topology, controls, staffing, and vendor terms are known through OI-018/OI-020.

The approved continuity criteria are 99.5% monthly signing availability, 99% monthly onboarding availability, a two-hour RPO, synchronous transactions preferred, and permission to pause all new onboarding during an interruption. Those criteria do not prove achieved service levels and do not define evidence-readiness or backlog-clearance time.

## Evidence And Limits

Primary navigation: [Product Value report](reviewer-reports/product-value/report.md), [capability matrix](controls/product/capability-contract-matrix.md), [product flow](controls/product/diagrams/product-value-flow.md), [rules/output semantics](controls/product/rules-and-output-semantics.md), [Revenue Risk report](reviewer-reports/revenue-risk/report.md), and canonical [open items](controls/open-items.md).

The [API-equivalent cost estimate](controls/cost-estimate.md) is **Unreconciled**: two auditor-authorized Terra passes exactly reconcile a USD 151.4883488 subtotal for the 28 included sessions, while one collector remains outside the total because its terminal lifecycle cutoff is missing. It is not a Codex invoice.

No target client, safe demo environment, customer observation, approved identity fixture, live artifact, Pro implementation, operative agreement, or specialist acceptance was inspected. The audit makes no legal, compliance, KYC, privacy, customer-acceptance, or production-readiness claim.

Structural validation not run: the canonical validator is absent from the active audit root.
