# Revenue-Critical Demo Readiness

## Current Status

No organization-owned revenue-critical demo is evidenced as ready. This is not a conclusion that the product cannot be demonstrated: the audit did not authorize a safe environment, test identity, fixture, target client, external demo inspection, or live execution. The repository's public demo link and source-visible paths are navigation, not organization demo acceptance. See [RR-E-009](../../evidence/packets/revenue-risk-claim-demo-commercial.md).

## Demo Acceptance Matrix

| Demo objective | Required evidence | Current state | Stop condition before external claim | Closure route |
|---|---|---|---|---|
| Show Community browser signing core | Pinned deployed digest/config; safe template, signer identities, disclosure mode; expected state/event/output oracle | Source path only | Do not claim organization readiness or accepted evidence | OI-010/OI-009 |
| Show organization web onboarding | Versioned API or embed client; entitlement; identity/KYC boundary; callback and readiness gate | Client and contract not supplied | Do not present vendor demo or checked-in OpenAPI as the target integration | OI-005/OI-010/OI-011 |
| Show organization mobile onboarding | Supported iOS/Android wrapper/component versions; lifecycle, callback, resume, accessibility, and device results | Unobserved external/Pro boundary | Do not claim supported mobile completion from public guide text alone | OI-005/OI-010 |
| Show completed evidence package | Result, combined document when applicable, audit PDF, hashes/signatures/TSA, known/altered verification results | Mechanisms source-visible; no accepted fixture | Do not call output legally valid, immutable, tenant-proven, or independently accepted | OI-002/OI-006 |
| Show interruption and recovery | Safe pause, committed-work inventory, aligned restore/replay, downstream reconciliation, controlled resume | Targets only; no drill | Do not claim availability/RPO achievement or no-loss recovery | OI-003/OI-014 |
| Show Pro/edition behavior | Release-specific entitlement, actual component, vendor evidence, sandbox terms and safe credential handling | Pro implementation unavailable | Do not simulate unavailable Pro behavior as product proof | OI-001/OI-005/OI-020 |

## Retained Demo Packet

OI-010 should retain, for each approved functional web/mobile golden path and material functional-failure case:

1. source, image digest, edition, license/entitlement, component/client versions, and target configuration;
2. sanitized template and identity/document fixtures with reset and expiry rules;
3. expected actor, disclosure, identity, completion-readiness, artifact, delivery, and downstream state;
4. timestamps, event/attempt records, output hashes, signed/unsigned artifacts, screenshots or recordings where permitted, and pass/fail results;
5. links to capacity/failure/recovery results owned by OI-003/OI-006 and business-exposure results owned by RR-OI-002; low/base/high evidence is required here only when the demo makes a workload, availability, recovery, or catch-up claim;
6. approved claim wording and authority sign-off, separated from the evidence itself.

No procedure in this audit was executed, and this control does not authorize production, customer, credential, or destructive actions.
