# PDR-013: Customer Document Intake

- Status: observed
- Evidence cutoff: Community source effective 2026-08-03

## Decision Statement

Community supports generic signer file/image attachment intake with a dangerous-extension denylist, but the inspected source does not classify an attachment as verified KYC evidence or implement a source-proven KYC document decision.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Product behavior/promise | Public pages position DocuSeal for onboarding/KYC and advanced ID verification. | PV-E-005 | Edition/service applicability unknown. |
| Implementation | File/image field upload, extension filtering, and blob storage exist. | PV-E-008 | No malware/content authenticity or KYC binding proof. |
| Runtime/demonstration | unknown | No document fixture | Rejection, scanning, storage, and privacy outcomes unobserved. |
| Approval/specialist sign-off | unknown | Audit mandate | KYC/privacy/security acceptance absent. |

## Constraints, Options, And Tradeoffs

Generic attachments can collect supporting files, but a regulated identity-document pipeline also needs accepted formats, malware/content checks, authenticity/identity binding, fallback, privacy, retention, and evidence semantics.

## Impacts And Boundaries

The target architecture must not treat a successfully stored attachment as an authenticated KYC document.

## Change, Reversal, And Follow-Up

Define the KYC document intake/verification boundary, assign Community versus vendor/organization controls, and run safe malicious/invalid/valid/privacy/retention fixtures with specialist approval.
