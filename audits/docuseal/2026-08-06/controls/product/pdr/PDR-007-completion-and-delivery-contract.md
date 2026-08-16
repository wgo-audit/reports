# PDR-007: Completion And Delivery Contract

- Status: observed
- Evidence cutoff: Community source effective 2026-08-03

## Decision Statement

Signer/submission completion is persisted before asynchronous result, combined document, audit, email, and webhook work; there is no single source-proven externally consumable readiness state.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Product behavior/promise | Completion enables downloads, emails, API/webhooks. | README, OpenAPI, PV-E-005 | Promise not atomicity guarantee. |
| Implementation | SQL completion and Sidekiq finalization are distinct. | PV-E-001; E-014 | Reconciliation/runtime unknown. |
| Runtime/demonstration | unknown | No queue/failure fixture | Delay, duplication, lost work unknown. |
| Approval/specialist sign-off | unknown | No business readiness contract | Revenue trigger not approved. |

## Constraints, Options, And Tradeoffs

Async work improves responsiveness but requires readiness, retry, reconciliation, and consumer idempotency semantics.

## Impacts And Boundaries

The organization must not equate `submission.completed_at` with evidence package delivered/verified without a proved contract.

## Change, Reversal, And Follow-Up

Define a readiness state/API, reconcile jobs/artifacts/delivery, and test crash/retry/exhaustion before customer onboarding use.
