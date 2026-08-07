# PDR-005: API And Webhook Contract Boundary

- Status: observed
- Evidence cutoff: Community source effective 2026-08-03; public pages post-cutoff validation

## Decision Statement

Community contains REST and webhook mechanisms, but the checked-in hosted OpenAPI, README, public pricing, and Pro error paths do not establish one release- and edition-specific integration contract.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Product behavior/promise | API/webhooks support integrations; public pricing calls API/embedding Pro. | PV-E-003/PV-E-005 | Dynamic and not release-bound. |
| Implementation | Community controllers/serializers and HMAC/retry delivery exist; some documented paths return Pro errors. | PV-E-003 | Entitlement/support unknown. |
| Runtime/demonstration | unknown | No client/consumer fixture | Ordering, replay, compatibility unobserved. |
| Approval/specialist sign-off | unknown | OI-001/OI-005 | Target contract not approved. |

## Constraints, Options, And Tradeoffs

Direct coupling is fastest but inherits vendor contract ambiguity. An organization adapter can isolate change and entitlement at additional maintenance cost.

## Impacts And Boundaries

Revenue-critical onboarding must not bind to checked-in OpenAPI or webhook success semantics as definitive Community behavior without vendor confirmation and contract tests.

## Change, Reversal, And Follow-Up

Obtain versioned OpenAPI/webhook schemas, edition entitlements, deprecation/support, idempotency/order/replay evidence; approve direct versus adapter integration.
