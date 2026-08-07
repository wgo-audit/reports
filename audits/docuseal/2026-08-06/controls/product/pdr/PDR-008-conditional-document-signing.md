# PDR-008: Conditional Document Signing

- Status: observed
- Evidence cutoff: Community source effective 2026-08-03

## Decision Statement

Generated result PDFs always receive a stored SHA-256, but cryptographic PDF signing occurs only when a signing reason and PKCS material are both available; trusted timestamping is optional.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Product behavior/promise | README says automatic PDF eSignature and verification. | `README.md:35-47` | Does not disclose conditional modes. |
| Implementation | Signed and unsigned branches, PKCS chain, optional TSA, SHA-256 metadata. | PV-E-004 | Certificate authority/custody unknown. |
| Runtime/demonstration | unknown | No output fixture | Signature profile/validation unobserved. |
| Approval/specialist sign-off | unknown | OI-002/OI-006 | Legal/CISO trust acceptance absent. |

## Constraints, Options, And Tradeoffs

Optional signing permits basic deployments but can silently produce outputs below an organization's evidentiary requirement unless configured to fail closed.

## Impacts And Boundaries

Visual signer marks, generated-file hashes, embedded PDF signatures, TSA timestamps, and legal signatures are distinct claims.

## Change, Reversal, And Follow-Up

Choose mandatory mode, certificate/key/TSA custody, revocation/LTV and outage policy; test independent verification of retained artifacts.
