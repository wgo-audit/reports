# Product Decision Candidate Inventory

## Coverage Domains

| Domain | Evidence boundary | Candidate count | Limitation/closure |
|---|---|---:|---|
| Maturity / demonstration | Pinned source, CI, no executable observation | 2 | Controlled fixtures and device runs are required. |
| Users / workflows | Signer, operator, API, webhook, embed, signature interaction source | 5 | Target actors, customer acceptance, consent/intent, and Pro implementation unknown. |
| Lifecycle | Template, submission, submitter, completion, archive/delete | 3 | Failure/recovery and production state unobserved. |
| Configuration / persistence | Template snapshots, identity preferences, certificate/TSA | 1 | Live values and authority approval unknown. |
| Outputs / provenance | Result, audit, hashes, verifier, downloads | 5 | No generated artifact or immutable evidence test. |
| Identity / governance / specialist | Community ability, email OTP, Pro identity, KYC attachment intake | 4 | KYC/legal/compliance and Pro validation deferred. |
| External dependencies / promises / acceptance | External embeds, public site, GitHub leads | 2 | Dynamic promises are not release contracts or acceptance. |

## Decision Candidates

| Candidate ID | Decision or durable behavior | Domain | Evidence | Observed/approved status | Disposition | Record or closure |
|---|---|---|---|---|---|---|
| PROD-DC-001 | Signing proceeds through public signer links, validated values/events, per-signer completion, then submission completion and async finalization. | users/workflow; lifecycle | PV-E-001 | observed; approval unknown | record-created | [PDR-001](pdr/PDR-001-signer-lifecycle-and-completion.md) |
| PROD-DC-002 | The organization-facing product has no demonstrated golden path in this audit. | maturity/demo | Audit brief; no approved safe environment/identity/fixture | evidence state; not a product decision | not-a-decision | Run controlled web/mobile fixtures before acceptance. |
| PROD-DC-003 | Submission creation conditionally snapshots template fields/schema and otherwise allows fallback to mutable template data. | configuration/lifecycle | E-012; `create_from_submitters.rb:22-77,224-246`; `submission.rb:127-175` | observed; rationale/approval unknown | record-created | [PDR-002](pdr/PDR-002-in-flight-template-contract.md) |
| PROD-DC-004 | Community operators have one enabled `admin` role with broad account management. | users/governance | PV-E-002 | observed; target approval unknown | record-created | [PDR-003](pdr/PDR-003-community-operator-access.md) |
| PROD-DC-005 | Signer email OTP is implemented, while phone/SMS identity, SAML, and granular roles are Pro/unavailable boundaries. | identity/governance | PV-E-002 | observed Community boundary; Pro unknown | record-created | [PDR-004](pdr/PDR-004-identity-assurance-edition-boundary.md) |
| PROD-DC-006 | Community contains REST and webhook mechanisms, but checked-in/public contracts are not release/edition-bound and include Pro/hosted paths. | workflow/external dependency | PV-E-003; E-012 | observed conflict; entitlement approval unknown | record-created | [PDR-005](pdr/PDR-005-api-and-webhook-contract-boundary.md) |
| PROD-DC-007 | External embedded web/mobile components are Pro dependencies; Community embed scripts are upgrade placeholders. | external dependency/workflow | PV-E-003/PV-E-005 | observed boundary; external behavior unknown | record-created | [PDR-006](pdr/PDR-006-embedded-web-mobile-boundary.md) |
| PROD-DC-008 | SQL completion precedes result/audit/email/webhook finalization; consumers need an explicit readiness contract. | lifecycle/output | PV-E-001; E-014 | observed; target contract unknown | record-created | [PDR-007](pdr/PDR-007-completion-and-delivery-contract.md) |
| PROD-DC-009 | Result PDFs are hashed; cryptographic signing is conditional on signing reason and PKCS, with optional TSA. | output/configuration | PV-E-004; E-015 | observed; live configuration/acceptance unknown | record-created | [PDR-008](pdr/PDR-008-conditional-document-signing.md) |
| PROD-DC-010 | Audit PDF is a generated snapshot of relational workflow/events and is optionally signed. | output/provenance | PV-E-004; E-015 | observed; immutability/authority unknown | record-created | [PDR-009](pdr/PDR-009-audit-evidence-snapshot.md) |
| PROD-DC-011 | Verification reports global generated-hash membership separately from PDF signature messages under the current account trust store. | output/provenance | PV-E-004 | observed; acceptance unknown | record-created | [PDR-010](pdr/PDR-010-verification-result-semantics.md) |
| PROD-DC-012 | Archive and permanent deletion have different evidence-retention consequences. | lifecycle/persistence | E-013; architecture data packet section 12 | observed; policy unknown | merged-into | PDR-009; organization retention/legal-hold decision and lifecycle tests. |
| PROD-DC-013 | Public pages promise legally binding/compliant signing, identity/integrity evidence, and independent verification beyond inspected proof. | public promise/specialist | PV-E-005 | observed promise; specialist approval unknown | record-created | [PDR-011](pdr/PDR-011-public-assurance-claim-boundary.md) |
| PROD-DC-014 | Partial signed-document visibility is a material acceptance scenario. | output/acceptance | PV-E-006 issue #384; per-submitter result generation | reporter lead plus source possibility | deferred | Reproduce on 3.1.7 and obtain product/legal policy; do not adopt issue conclusion. |
| PROD-DC-015 | Reported signature timestamp mismatch is a material artifact test scenario. | output/acceptance | PV-E-006 issue #575 | reporter lead; issue closed | deferred | Reproduce with controlled fixtures across signer roles/timezones. |
| PROD-DC-016 | API-created submitters may be marked completed and logged as `api_complete_form`. | workflow/identity | `api/submissions_controller.rb:217-252`; OpenAPI `completed` field | observed; target authorization/intent policy unknown | merged-into | PDR-005 and PDR-004; define server-side signing authority. |
| PROD-DC-017 | Webhook HMAC has a five-minute verifier tolerance and retries are at-least-once from the consumer perspective. | rules/output | PV-E-003 | observed; consumer policy unknown | merged-into | PDR-005; require dedupe/replay/version policy. |
| PROD-DC-018 | Public/mobile guides describe hosted API and iOS WebView integration but do not bind to self-hosted Community 3.1.7. | promise/external dependency | PV-E-005 | observed promise; compatibility unknown | merged-into | PDR-006; vendor-supported device/package matrix. |
| PROD-DC-019 | Customer/operator acceptance criteria are not present in approved evidence. | acceptance | Audit brief and source boundary | unknown | blocked | Product Manager defines actor/device/error/evidence acceptance before test execution. |
| PROD-DC-020 | Legal validity, KYC sufficiency, data-residency, and Community/Pro approval are assigned to external authorities by the mandate. | specialist/governance | Audit brief | explicitly unapproved | deferred | Route to legal, compliance, privacy, CISO, Product, and VP Engineering. |
| PROD-DC-021 | Signature fields support drawn, typed, uploaded/camera, and reusable signature images; the disclosure link is conditional, defaults false, and is not enabled by the Community form partial. | users/workflow; governance | PV-E-007 | observed implementation; consent/intent/legal approval unknown | record-created | [PDR-012](pdr/PDR-012-signature-capture-and-disclosure.md) |
| PROD-DC-022 | Generic file/image attachment intake exists, but no inspected Community rule classifies an attachment as verified KYC evidence. | identity/workflow | PV-E-008 | observed upload; KYC semantics/approval unknown | record-created | [PDR-013](pdr/PDR-013-customer-document-intake.md) |

All material `record-created` candidates have individual PDRs. The number of records reflects independently changeable product contracts rather than a target count.
