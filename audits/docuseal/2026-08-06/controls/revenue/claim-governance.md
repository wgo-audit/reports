# Revenue Claim Governance

Coordinator mapping: local RR-OI-001 is serialized as canonical OI-023. Local labels remain below for traceability to the reviewer draft.

## Purpose And Evidence Boundary

This control prevents implementation, vendor positioning, target intent, demonstration, authority acceptance, and operating performance from being collapsed into one commercial claim. It covers DocuSeal Community `3.1.7` and the approved evidence summarized in the [Revenue Risk packet](../../evidence/packets/revenue-risk-claim-demo-commercial.md). It is an audit control design, not an approved marketing, legal, compliance, sales, contract, or production policy.

## Claim Decision Rule

A claim is eligible for authority review only when every applicable gate is evidenced:

`claim eligibility = implementation applicability ∧ release/edition entitlement ∧ demonstrated behavior ∧ authority acceptance ∧ operating evidence ∧ current commercial terms`

This is a logical gate, not a statement that a claim becomes legally or commercially acceptable automatically. A non-applicable gate must be explicitly justified by the named claim authority rather than silently removed.

## Current Claim Register

| Candidate claim | Current evidence-bounded wording | Gates still open | Current disposition | Required route |
|---|---|---|---|---|
| “DocuSeal has an inspectable signing core.” | Community `3.1.7` source implements template-driven multi-party signing, required-field validation, completion state, output/audit work, downloads, API serialization, and webhooks. | Organization demonstration, acceptance, target suitability | Usable only for further-evaluation discussions | E-025/E-027 and OI-010 |
| “Our web/mobile onboarding is supported.” | Public and checked-in material describe web/mobile and API/embed integration; required target paths cross unresolved release, edition, package, and entitlement boundaries. | Vendor contract matrix, package provenance, target-client demonstration, customer acceptance | Not approved | OI-001/OI-005/OI-010/OI-020 |
| “A completed submission is ready for customer activation or revenue gating.” | Relational completion precedes asynchronous result/audit, mail, and webhook finalization. | Organization readiness state, downstream reconciliation, failure/catch-up proof | Not approved | OI-009/OI-003/OI-014 |
| “Signatures are legally binding/compliant.” | Source exposes signature images, conditional PDF signing, optional TSA, audit generation, and verifier mechanisms. | Jurisdiction, disclosure/intent, identity/KYC, artifact, trust, retention, and authority acceptance | Prohibited as an audit or production conclusion | OI-002/OI-006/OI-009/OI-011 plus legal/compliance/CISO review |
| “Signer identity/KYC is verified.” | Community implements email possession and generic attachments; advanced identity methods are unresolved/Pro boundaries. | Transaction-tier assurance, document authenticity, identity binding, privacy/retention, vendor evidence | Not approved | OI-011/OI-002/OI-005 |
| “Signed artifacts are independently verifiable and tamper-evident.” | Result hashes, conditional PDF signatures, generated audit PDF, and signature verification are distinct source mechanisms. | Known/altered/cross-tenant/revoked artifact tests, tenant provenance, trust-root/TSA, immutability and specialist acceptance | Not approved | OI-002/OI-006 |
| “Signing meets 99.5% monthly availability; onboarding meets 99%.” | These percentages are approved target criteria. | Measurement rules, customer-visible indicators, target operation, retained monthly results | Target language only; achievement claim prohibited | OI-014/OI-003 |
| “Recovery loses no more than two hours.” | Two hours is the approved RPO; synchronous transactions are preferred. | Aligned SQL/blob/key recovery, queue/artifact reconciliation, restore exercise | Target language only; achievement claim prohibited | OI-003/OI-006 |
| “Community/Pro commercial continuity is assured.” | Public prices and terms expose commercial signals; self-hosting leaves operating/control duties to the organization, while assigned and effective ownership is unproved. | Operative agreement, entitlement, support/renewal/interruption terms, owner and transition proof | Not approved | OI-019/OI-020/OI-013 |
| “The organization has a production-ready demo.” | No safe organization environment, identity, fixture, supported client, reset, failure proof, or retained artifact package was observed. | All demo-readiness gates | Not approved | OI-010 and [`demo-readiness.md`](demo-readiness.md) |

## Required Claim Record

Before a claim is used in sales, procurement, executive approval, customer communication, compliance mapping, incident communication, or renewal, retain:

| Field | Minimum content |
|---|---|
| Claim ID and exact wording | No paraphrase drift; include prohibited implications. |
| Audience and use | Internal evaluation, executive decision, sales/demo, customer contract, incident, regulator, or public marketing. |
| Product boundary | Release/commit, Community/Pro/Cloud, target architecture, client/component versions. |
| Evidence | Direct source, retained demo/output, measurement period, specialist/vendor record, and expiry. |
| Authority | Product, Engineering, Operations, CISO, legal/compliance, procurement/commercial as applicable. |
| Conditions and exclusions | Identity tier, jurisdiction, transaction class, availability calculation, customer boundary, fallback. |
| Revalidation trigger | Release, configuration, provider, contract, identity/signing policy, target architecture, or evidence expiry. |

## Material Open Routes

| Placeholder | Type / priority | Item and consequence | Proposed owner | Closure route |
|---|---|---|---|---|
| RR-OI-001 | decision-needed / P1 | Approve a claim register and authority matrix for signing, identity/KYC, artifact integrity, web/mobile/API/embed applicability, availability/RPO, and commercial continuity. Without it, vendor or internal language can become an unsupported sales, onboarding, renewal, incident, or regulatory assertion. | Product Manager with CISO, legal/compliance authority, VP Software Engineering, IT Operations Director, and commercial authority | Populate this register with exact claims, release/edition/evidence gates, named approvers, expiry, prohibited implications, and revalidation triggers; retain approvals. |

Existing OI-009 owns the customer-facing workflow and authoritative readiness/revenue gate; OI-010 owns golden-path demonstration; OI-001/OI-005/OI-020 own edition, contract, and vendor proof. RR-OI-001 must not duplicate those facts—it governs when their results permit a claim.
