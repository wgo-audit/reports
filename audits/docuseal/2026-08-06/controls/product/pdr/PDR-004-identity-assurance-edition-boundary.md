# PDR-004: Identity Assurance Edition Boundary

- Status: observed
- Evidence cutoff: Community source effective 2026-08-03

## Decision Statement

Community implements signer email OTP/link assurance, while phone/SMS verification, SAML SSO, granular roles, ID verification, KBA, AES/QES, or equivalent advanced assurance cannot be concluded from the inspected Community implementation.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Product behavior/promise | Email/SMS authentication and higher-assurance methods are publicly described. | PV-E-005 | Mixes plans/services; assurance unproved. |
| Implementation | Email OTP exists; SSO/SMS UI is Pro placeholder; advanced event vocabulary alone is not implementation. | PV-E-002 | Pro implementation out of scope. |
| Runtime/demonstration | unknown | No identity fixture | Channel possession and failure behavior untested. |
| Approval/specialist sign-off | unknown | Mandate reserves KYC/legal determinations | Cannot infer sufficiency. |

## Constraints, Options, And Tradeoffs

Email OTP is available without Pro dependence but may not satisfy the organization's KYC binding. Higher assurance adds vendor/external dependencies and specialist requirements.

## Impacts And Boundaries

The target onboarding design cannot assume phone, SSO, roles, ID, KBA, AES, or QES until vendor evidence and authority acceptance exist.

## Change, Reversal, And Follow-Up

Legal/compliance/CISO define assurance tiers; vendor supplies edition-specific method, provider, evidence payload, failure, retention, and pricing details; organization tests them.
