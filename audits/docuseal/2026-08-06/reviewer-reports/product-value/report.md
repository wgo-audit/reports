# Product Value

## Audit Question, Depth, And Evidence Boundary

At detailed depth, this review asks what customer and business value DocuSeal Community `3.1.7` demonstrably implements for regulated SaaS web/mobile onboarding, where the workflow is partial, and where public promise, Pro entitlement, demonstration, customer acceptance, or specialist sign-off remains unresolved. Evidence is pinned source at `a2d8b855491793870b7b4acf176d2d95ae95ff83`, E-001/E-010–E-018, [direct Product Value inspection](../../evidence/packets/product-value-source-inspection.md), approved `docuseal.com` pages used only as post-cutoff validation, and the shared GitHub packet. Pro implementation, hosted Cloud, live operation, target configuration, customer acceptance, legal/regulatory conclusions, and penetration/load testing are excluded.

One CodeGraph preflight used the absolute Git root and `--path`; it confirmed the indexed completion/API/webhook topology but did not provide runtime proof. No golden-path observation was authorized because no safe environment, test identity, or fixture was approved.

## Coverage And Material Gaps

The review traced actors and entry points; template/submission/signer lifecycle; ordering, validation, signature modalities, conditional disclosure, email OTP and completion; customer attachment/KYC-document boundaries; API, webhooks and external embedding; Community/Pro identity and permissions; result/audit generation; downloads and verification; public mobile/regulatory promises; and reporter-supplied issue leads. The mandated deep-review trigger is met because the capability crosses UI/API/embed entry points, multiple actors and lifecycle states, asynchronous dependencies, identity rules, document/audit outputs, and public/edition contracts.

Material gaps are target web/mobile demonstration, release-specific entitlement/contracts, advanced identity implementation, end-to-end failure/readiness behavior, signed and unsigned artifact fixtures, evidence immutability/tenant binding, customer acceptance, and specialist decisions. These are routed through existing OI-001/OI-002/OI-005/OI-006 and the proposed Product Value items below.

## Key Findings

| Finding | Severity | Effort | Evidence links | Confidence and limitation | Consequence |
|---|---|---|---|---|---|
| Core template-to-multi-signer completion is materially implemented, but no organization-facing web/mobile golden path was demonstrated. | High | M | [PV-E-001](../../evidence/packets/product-value-source-inspection.md); [flow](../../controls/product/diagrams/product-value-flow.md) | High source confidence; runtime/device/customer behavior unknown. | The repository can support further evaluation, but it cannot yet support an onboarding acceptance claim. |
| Signature image capture supports multiple modalities, but disclosure is conditional/default-off in Community and no durable consent/intent acceptance record was found. | High | M | [PV-E-007](../../evidence/packets/product-value-source-inspection.md); [PDR-012](../../controls/product/pdr/PDR-012-signature-capture-and-disclosure.md) | High source confidence; policy, runtime comprehension, and legal acceptance unknown. | A signature image or completion event cannot be promoted to proof of disclosure, consent, intent, identity, or legal effect. |
| Community has one broad operator role and email OTP; granular roles, SAML, SMS/phone assurance, and external embedding are Pro/unavailable boundaries. | High | M | [PV-E-002](../../evidence/packets/product-value-source-inspection.md); [PDR-003](../../controls/product/pdr/PDR-003-community-operator-access.md); [PDR-004](../../controls/product/pdr/PDR-004-identity-assurance-edition-boundary.md) | High Community boundary confidence; Pro behavior and KYC sufficiency unknown. | Community alone does not establish least-privilege or required signer identity assurance at the stated scale. |
| Community generic file/image intake and extension filtering do not constitute a verified KYC-document pipeline. | High | M | [PV-E-008](../../evidence/packets/product-value-source-inspection.md); [PDR-013](../../controls/product/pdr/PDR-013-customer-document-intake.md) | High source confidence; malware/content/authenticity/identity/privacy acceptance unknown. | Successfully stored attachments could be mistaken for authenticated KYC evidence. |
| API/webhook mechanisms exist in Community, but checked-in OpenAPI, public pricing, Pro error paths, and embedding placeholders do not form one release/edition contract. | High | M | [PV-E-003/PV-E-005](../../evidence/packets/product-value-source-inspection.md); [matrix](../../controls/product/capability-contract-matrix.md) | High conflict confidence; entitlement/support/Pro implementation unknown. | The required web/mobile integration could bind to unavailable, unsupported, or version-incompatible behavior. |
| Submission completion is not evidence-package readiness: result/audit/email/webhook finalization follows asynchronously. | High | M | [PV-E-001](../../evidence/packets/product-value-source-inspection.md); E-014; [PDR-007](../../controls/product/pdr/PDR-007-completion-and-delivery-contract.md) | High source confidence; recovery and live delay unknown. | A premature revenue/onboarding trigger can advance before required documents, audit, or notifications are ready. |
| Result PDFs may be hashed but unsigned; embedded signing requires reason plus PKCS and optional TSA, while audit signing is separately conditional. | High | M | [PV-E-004](../../evidence/packets/product-value-source-inspection.md); E-015; [PDR-008](../../controls/product/pdr/PDR-008-conditional-document-signing.md) | High implementation confidence; no keys, TSA, output, or trust acceptance. | Visual signatures, hashes, PKI signatures, trusted timestamps, and legal signatures cannot be collapsed into one “signed” state. |
| Audit evidence is a generated relational-state snapshot, and API verification's checksum result is global membership without tenant/submission provenance. | High | L | [PV-E-004](../../evidence/packets/product-value-source-inspection.md); [PDR-009](../../controls/product/pdr/PDR-009-audit-evidence-snapshot.md); [PDR-010](../../controls/product/pdr/PDR-010-verification-result-semantics.md) | High source confidence; no artifact, immutability, restore, or specialist test. | The available mechanisms do not by themselves establish independently preserved, tenant-bound evidentiary integrity. |
| Public legal/compliance/independent-verification claims exceed what the inspected Community source and approved evidence establish. | High | M | [PV-E-005](../../evidence/packets/product-value-source-inspection.md); [PDR-011](../../controls/product/pdr/PDR-011-public-assurance-claim-boundary.md) | High confidence in observed promise; release/edition applicability and authority acceptance unknown. | Adopting vendor language as an audit conclusion would misstate regulatory and production readiness. |
| Conditional template snapshot/fallback semantics lack explicit version binding for in-flight submissions. | Medium | M | E-012; [PDR-002](../../controls/product/pdr/PDR-002-in-flight-template-contract.md) | High source confidence; change-during-signing behavior unobserved. | Later template edits may create uncertain in-flight contract/evidence semantics. |

## Mandate-Relevant Strengths

- The repository exposes a coherent, inspectable signing workflow with multi-party ordering, required-field validation, signer event capture, output generation, downloads, API serialization, and webhook delivery.
- Community implements signer email OTP, result hashes, optional PKCS/TSA signing, a detailed audit PDF, and PDF signature verification mechanisms; these provide concrete mechanisms to validate rather than only marketing descriptions.
- Edition placeholders and Pro error paths make several unavailable boundaries directly visible, allowing vendor questions to be specific without treating unavailable Pro code as a Community defect.
- Pinned source and direct output semantics support reproducible controlled artifact tests.

### Decision Insights

1. **Edition/integration decision:** the core workflow is inspectable, but the required embedded web/mobile, API contract, roles, SAML, and SMS identity outcome crosses Pro boundaries. Choosing Community before a release-specific contract risks redesign; the smallest next proof is a vendor-supplied entitlement/component/compatibility matrix plus package provenance.
2. **Onboarding completion decision:** SQL completion precedes evidence and delivery finalization. Using `completed_at` as the customer/revenue gate can advance an incomplete evidence package; define and test an organization-owned readiness state with reconciliation.
3. **Identity decision:** Community email OTP proves a channel-possession step, while KYC binding and advanced methods are unproved. A wrong assumption could invalidate the onboarding control design; legal/compliance/CISO must define assurance tiers before vendor method selection.
4. **Evidence/trust decision:** conditional PKI signing, snapshot audit generation, and unscoped hash membership are distinct mechanisms. Treating them as independent legal verification could overstate evidence; test signed/unsigned artifacts under approved trust roots and design tenant-bound provenance/retention.
5. **Proceed/stop decision:** no source evidence currently proves a fatal absence in the Community signing core, while several material requirements remain decision dependencies. The evidence supports continued evaluation conditionally—not production approval—provided edition, identity, readiness, artifact, and specialist gates precede commitment.

## Selected Outputs

- [Product decision candidate inventory](../../controls/product/pdr-candidate-inventory.md)
- [Product decision register](../../controls/product/pdr-register.md) and all 13 linked PDRs
- [Capability and contract matrix](../../controls/product/capability-contract-matrix.md)
- [Product Value flow](../../controls/product/diagrams/product-value-flow.md)
- [Rules and output semantics](../../controls/product/rules-and-output-semantics.md)
- [Provenance notes](../../controls/product/provenance-notes.md)
- [Direct evidence packet](../../evidence/packets/product-value-source-inspection.md)

The complete deep-review packet was triggered and produced. The flow is source-bounded because no live evidence was authorized; unknown edges are shown explicitly.

## Material Omissions, Unknowns, And Auditor Questions

### Open items after coordinator serialization

| Placeholder | Type | Priority | Item and consequence | Owner | Closure route |
|---|---|---|---|---|---|
| OI-009 | decision-needed | P1 | Approve the customer-facing signing contract: actor/order, signature modality, disclosure/consent/intent evidence, partial-document visibility, authoritative completion/readiness state, output package, and correction/expiry/decline/delegation behavior. Without it, tests and revenue gating have no acceptance oracle. | Product Manager, VP Software Engineering, legal/compliance authority | Publish approved workflow and evidence acceptance criteria, then bind implementation tests to them. |
| OI-010 | verification | P1 | Demonstrate the approved golden path and material failures on supported web/iOS/Android actors, including signature/disclosure modes, identity and KYC-document challenges, ordered/parallel signers, retries, partial/completed downloads, audit, webhooks, altered artifacts, and upgrade compatibility. | Product Manager, VP Software Engineering, CISO | Use safe identities/documents/fixtures in an approved environment; retain outputs, event records, versions, and pass/fail results. |
| OI-011 | decision-needed | P1 | Select signer identity-assurance tiers and determine their KYC/jurisdiction sufficiency; email possession, SMS, ID/KBA/AES/QES, and operator identity are not interchangeable. | CISO with legal/compliance authority and Product Manager | Map transaction classes to assurance, consent, evidence, fallback, privacy, and retention requirements; then validate vendor methods. |

Existing OI-005 should absorb the release-specific API/webhook/embed/Pro contract evidence. Existing OI-002/OI-006 should absorb signed/unsigned artifact trust, tenant-bound provenance, immutability, retention, restore, deletion, and specialist acceptance tests. No qualifying auditor question was found: the unresolved matters are proof or named-authority decisions, not a mandate/priority/authority answer the auditor can supply.

## Reconciliation

No material prior Product Value item existed. Architecture's Community/API mismatch, Pro embed boundary, conditional signing, snapshot audit, async completion, and target/live limits were verified against direct source and retained. Public pricing and compliance pages conflict with neither source implementation nor entitlement by themselves; they create an applicability/promise gap. GitHub issues #384, #575, and #507 remain reporter leads and test cases, not confirmed defects or legal/contract conclusions. No material evidence conflict was silently resolved.

The required bounded quality review found a disconnected flow representation and under-specified disclosure/consent, KYC attachment, evidence precision, and state classification. The selected outputs were revised once: exact node transitions replaced subgraph edges, PDR-012/PDR-013 and PV-E-007/PV-E-008 were added, public/absence/immutability wording was bounded, and the capability matrix now classifies each capability state. No unsupported quality concern was suppressed.

## Checklist Disposition

| Work item | State | Next action | Recommended next reviewer | Factual completion condition |
|---|---|---|---|---|
| `product-value` | `completed-with-open-verification` | Coordinator serializes proposed PV evidence/open items and carries edition, golden-path, identity, readiness, artifact, and specialist gates | `expense-exposure`, `scalability` | Report, handoff, 22-candidate inventory, 13-record register/PDRs, complete four-artifact deep-review packet, source-bounded views, material omissions, and reconciliation complete; Pro/live/customer/specialist proof remains open |

Structural validation not run: the canonical validator is absent from the active audit root.

## Bounded Conclusion And Downstream Guidance

DocuSeal Community `3.1.7` is a technically substantive foundation for further evaluation: the central multi-party signing, signature-image, attachment, event, output, API, webhook, hashing, optional signing, audit, and verification mechanisms are inspectable. Product readiness is nevertheless conditional. The required disclosure/consent/intent contract, KYC-document pipeline, embedded web/mobile integration, granular access, SSO/SMS/advanced identity, release-specific contracts, completion-readiness semantics, immutable tenant-bound evidence, artifact correctness, and legal/KYC/customer acceptance are not established. Product Value therefore supports **continue evaluation conditionally**, never production or regulatory approval.

Expense Exposure and Scalability may use the capability/contract matrix and completion flow to model Pro usage, integration dependencies, asynchronous work, and output volume. Business Continuity, Contributor/Vendor Value, and Revenue Risk should use the PDRs after their dependencies complete. They must not assume entitlement, live behavior, customer acceptance, artifact correctness, legal validity, compliance, or specialist approval.
