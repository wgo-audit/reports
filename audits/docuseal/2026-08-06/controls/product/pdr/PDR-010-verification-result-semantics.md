# PDR-010: Verification Result Semantics

- Status: observed
- Evidence cutoff: Community source effective 2026-08-03

## Decision Statement

The API verification tool reports whether uploaded bytes occur in a global generated-document hash table and separately returns embedded PDF signature verification messages using the current account trust store.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Product behavior/promise | README/public pages promise PDF signature/independent verification. | PV-E-005 | Promise does not define response semantics. |
| Implementation | Unscoped `CompletedDocument.exists?` plus account-trust signature messages. | PV-E-004 | No tenant/submission provenance response. |
| Runtime/demonstration | unknown | No known/altered/cross-tenant fixture | False-assumption boundary untested. |
| Approval/specialist sign-off | unknown | OI-002/OI-006 | Acceptance absent. |

## Constraints, Options, And Tradeoffs

Global membership is simple but does not establish who generated the file, for which submission/tenant, or that all signatures are trusted.

## Impacts And Boundaries

Consumers could overread `checksum_status=verified` as legal authenticity or tenant-bound provenance.

## Change, Reversal, And Follow-Up

Separate byte-membership, provenance, and signature-trust outcomes; bind tenant/submission/artifact identifiers and validate known/altered/cross-account/revoked cases.
