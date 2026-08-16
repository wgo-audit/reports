# Signing And Verification Trust Boundary

## Purpose And Evidence Boundary

- Reader question: Which inputs create signed/audit artifacts, where are trust decisions made, and what remains unknown for independent verification?
- Evidence cutoff: 2026-08-06; Community `3.1.7` / `a2d8b855…`.
- Confirmed notation: solid implemented source path.
- Inferred notation: dotted consequence requiring artifact/specialist validation.
- Unknown notation: dashed authority, key-custody or acceptance boundary.
- Evidence links: [data/jobs packet §5–8](../../../evidence/packets/architecture-data-jobs-migrations-provenance.md); [runtime packet §11, §15](../../../evidence/packets/architecture-runtime-deployment-delivery-identity-secrets.md); [ADR-007](../adr/ADR-007-signing-audit-and-verification-trust.md).

## Evidence Dimensions Used

Implementation is present. No live certificate/TSA/artifact, HSM/KMS, legal/compliance/security acceptance, or independent verifier observation was supplied.

## Diagram

```mermaid
flowchart TB
  subgraph INPUTS["Confirmed evidence inputs"]
    direction LR
    TEMPLATE["Template/source PDFs"]
    VALUES["Signer values and attachments"]
    EVENTS["SQL events, IP, user agent, session, timestamps"]
  end
  subgraph TRUST["Confirmed configurable trust inputs"]
    direction LR
    AUTOGEN["Setup-generated private CA chain"]
    PKCS["Uploaded PKCS12 plus password in encrypted config"]
    TSA["Optional timestamp service URL"]
  end
  subgraph GENERATE["Confirmed conditional generation stage"]
    direction LR
    SIGNED["Signed result/audit PDF when PKCS is configured"]
    UNSIGNED["Unsigned result/audit PDF when signing is not configured"]
    RHASH["Result PDF SHA-256 metadata and completion rows"]
    AHASH["Audit PDF has no same application SHA-256 at creation"]
  end
  subgraph VERIFY["Confirmed application verifier"]
    direction LR
    UPLOAD["Uploaded PDF"] --> GLOBAL["Global CompletedDocument hash-membership check"]
    UPLOAD --> SIGCHECK["Embedded-signature check against current account trust store"]
  end
  subgraph UNKNOWN["Unknown authority and preservation"]
    direction LR
    CUSTODY["HSM/KMS, rotation, revocation and recovery"]
    IMMUT["Immutable event/artifact retention and binding"]
    ACCEPT["Legal, compliance and security specialist acceptance"]
  end
  INPUTS --> GENERATE
  TRUST --> SIGNED
  SIGNED --> RHASH
  SIGNED --> AHASH
  UNSIGNED --> RHASH
  UNSIGNED --> AHASH
  RHASH -. "later uploaded result may match" .-> GLOBAL
  SIGNED -. "later uploaded signed PDF may be checked" .-> SIGCHECK
  TRUST -. "custody unproved" .-> CUSTODY
  GENERATE -. "preservation unproved" .-> IMMUT
  VERIFY -. "sufficiency unknown" .-> ACCEPT
```

## Known Gaps And Follow-Up

OI-002 must choose the trust/key/TSA model with specialists. OI-006 must verify signed and unsigned paths, timestamp failure behavior, the global hash query versus account-scoped trust, audit-artifact hashing, tenant/provenance binding, tamper detection, regeneration, immutable retention and independent verification. No legal or regulatory conclusion is made.
