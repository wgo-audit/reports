# ADR-010: Identity And Secret-Root Boundary

- Status: observed
- Evidence cutoff: 2026-08-06

## Decision Statement

Community human access uses Devise and CanCanCan with one declared admin role and optional TOTP enforcement. API access uses per-user bearer tokens without evidenced expiry/scopes. Environment/AWS/file bootstrap supplies `SECRET_KEY_BASE`; absent a separate `ENCRYPTION_SECRET`, that same root derives database encryption while also supporting session/token/signed-ID purposes.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Implementation | Admin-only role model, Devise/MFA, hashed+encrypted API token, environment/AWS/dotenv secret root and AR encryption | [Runtime packet §9–14](../../../evidence/packets/architecture-runtime-deployment-delivery-identity-secrets.md) | Pro SAML/roles unavailable; no key version/rotation path evidenced |
| Runtime/live state | unknown | No IdP, user, token, secret manager or key observation | Enforcement/custody unproved |
| Rationale | unknown | No identity/key architecture record | Defaults are not target policy |
| Approval | unknown | CISO/identity authority unavailable | Least privilege and rotation unapproved |

## Constraints, Options, And Tradeoffs

Community defaults are simple but do not establish enterprise joiner/mover/leaver, segregation, service identity or key rotation. Pro SSO/roles may change the boundary and require vendor validation. Separating encryption/signing/session purposes and using managed custody increases operational complexity but limits compromise blast radius.

## Impacts And Boundaries

Secret rotation is coupled to encrypted records, API tokens, webhook secrets, signing configuration, sessions and recovery. This record is architecture evidence, not a security-control effectiveness conclusion.

## Change, Reversal, And Follow-Up

OI-001 determines edition identity dependencies; OI-002 and OI-003 define key/secret custody, versioning, rotation, MFA/session/token policy and emergency access.

