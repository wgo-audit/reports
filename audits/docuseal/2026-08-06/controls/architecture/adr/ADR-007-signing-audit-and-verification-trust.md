# ADR-007: Signing, Audit, And Verification Trust

- Status: observed
- Evidence cutoff: 2026-08-06

## Decision Statement

Result and audit PDFs are cryptographically signed only when signing configuration is present; otherwise output can be written unsigned. The application can use a setup-generated private CA chain or an uploaded PKCS#12, optionally calls a TSA, stores hashes/events, renders an audit snapshot, and verifies uploaded PDFs against a hash registry plus the account trust store.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Implementation | Conditional PKCS signing/TSA, generated audit PDF, SHA-256 metadata/completion rows and verifier | [Data packet §5–8](../../../evidence/packets/architecture-data-jobs-migrations-provenance.md); [runtime packet §11, §15](../../../evidence/packets/architecture-runtime-deployment-delivery-identity-secrets.md) | Audit events are ordinary mutable SQL; configuration/live path unknown |
| Runtime/live state | unknown | No generated artifact, certificate, TSA or verifier observation | Correctness and trust chain untested |
| Rationale | unknown | No source-backed trust-policy record | Product wording is not specialist approval |
| Approval | unknown | Legal/compliance/security acceptance unavailable | No enforceability or regulatory conclusion |

## Constraints, Options, And Tradeoffs

Self-generated certificates can provide detectable PDF signatures without external public trust; externally trusted certificates/TSA/HSM can strengthen third-party verification but add custody, availability, cost and vendor dependencies. A snapshot audit PDF is convenient but is not itself an immutable event store.

## Impacts And Boundaries

This record does not establish legal validity, KYC binding, PAdES profile, LTV, tamper-proof retention or independent evidentiary sufficiency. The TSA handler's failure path and hash lookup binding require specialist validation. See the [trust diagram](../diagrams/signing-and-verification-trust-boundary.md).

## Change, Reversal, And Follow-Up

OI-002 requires an authority decision on certificate/key/TSA/trust model; OI-006 requires artifact/event immutability, retention and independent verification tests before production approval.

