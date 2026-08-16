# Product Decision Register

## Records

| ID | Statement | Domain | Status | Evidence confidence | Record link |
|---|---|---|---|---|---|
| PDR-001 | Source-visible signer lifecycle ends in asynchronous finalization. | workflow/lifecycle | observed | High for source; no runtime proof | [Record](pdr/PDR-001-signer-lifecycle-and-completion.md) |
| PDR-002 | In-flight submissions conditionally snapshot template contracts. | configuration/lifecycle | observed | High for source; rationale unknown | [Record](pdr/PDR-002-in-flight-template-contract.md) |
| PDR-003 | Community operator access is broad single-role administration. | identity/governance | observed | High for source; target fit unknown | [Record](pdr/PDR-003-community-operator-access.md) |
| PDR-004 | Email OTP is Community; advanced identity/access capabilities are Pro/unavailable. | identity/edition | observed | High boundary confidence; Pro unknown | [Record](pdr/PDR-004-identity-assurance-edition-boundary.md) |
| PDR-005 | API/webhook mechanisms and their documented/entitled contracts are not demonstrably aligned. | integration/contract | observed | High source-conflict confidence | [Record](pdr/PDR-005-api-and-webhook-contract-boundary.md) |
| PDR-006 | External embedded web/mobile signing is a Pro dependency. | workflow/dependency | observed | High boundary confidence; implementation unknown | [Record](pdr/PDR-006-embedded-web-mobile-boundary.md) |
| PDR-007 | Completion timestamp and output/delivery readiness are distinct states. | lifecycle/output | observed | High for source; operations unknown | [Record](pdr/PDR-007-completion-and-delivery-contract.md) |
| PDR-008 | Document cryptographic signing is configuration-conditional. | output/trust | observed | High for source; live trust unknown | [Record](pdr/PDR-008-conditional-document-signing.md) |
| PDR-009 | Audit evidence is a generated, optionally signed snapshot. | output/provenance | observed | High for source; authority unknown | [Record](pdr/PDR-009-audit-evidence-snapshot.md) |
| PDR-010 | Verification combines unscoped hash membership and account-trust signature messages. | output/verification | observed | High for source; acceptance unknown | [Record](pdr/PDR-010-verification-result-semantics.md) |
| PDR-011 | Public assurance claims remain promises pending edition-specific and specialist validation. | promise/governance | observed | High for observed wording; applicability unknown | [Record](pdr/PDR-011-public-assurance-claim-boundary.md) |
| PDR-012 | Signature-image capture and optional disclosure do not establish consent, intent, identity, or legal effect. | workflow/governance | observed | High for source; acceptance unknown | [Record](pdr/PDR-012-signature-capture-and-disclosure.md) |
| PDR-013 | Generic attachment intake is not a verified KYC document decision. | identity/workflow | observed | High for source; KYC semantics unknown | [Record](pdr/PDR-013-customer-document-intake.md) |

## Coverage And Disposition

| Domain | Candidates | Records | Other dispositions | Limitation |
|---|---:|---:|---|---|
| Maturity/demo | 2 | 0 | 1 not-a-decision, 1 blocked | No safe golden path or acceptance criteria. |
| Users/workflows | 5 | 4 | 1 merged | Target actors, consent/intent, and Pro behavior unknown. |
| Lifecycle | 3 | 3 | archive/delete merged into PDR-009 | Recovery/live behavior unobserved. |
| Configuration/persistence | 1 | 1 | related identity/output configuration covered in their domains | Live configuration and approval unknown. |
| Outputs/provenance | 5 | 4 | 1 webhook rule merged; reporter scenarios deferred | No generated fixtures or independent preservation. |
| Identity/governance/specialist | 4 | 4 | specialist determination deferred | KYC/legal/compliance approval absent. |
| Dependencies/promises/acceptance | 2 | 2 | mobile details merged | External packages and contracts out of scope. |
