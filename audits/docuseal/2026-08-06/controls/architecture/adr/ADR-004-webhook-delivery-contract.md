# ADR-004: Webhook Delivery Contract

- Status: observed
- Evidence cutoff: 2026-08-06

## Decision Statement

Webhook events are queued asynchronously, serialized into an event envelope, optionally HMAC-signed, retried exponentially, and recorded in event/attempt tables. Event UUID uniqueness is local; remote consumers still require idempotency and replay governance.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Implementation | Named event jobs, HMAC envelope, attempts/status and retries | [Component packet §7](../../../evidence/packets/architecture-component-api-ui-contracts.md); [data packet §9](../../../evidence/packets/architecture-data-jobs-migrations-provenance.md) | Docs and serializers are parallel contracts |
| Runtime/live state | unknown | No delivery logs or consumer evidence | Retry exhaustion and backlog unobserved |
| Rationale | unknown | No decision record found | Source shape does not prove intended SLA |
| Approval | unknown | No organization consumer contract | At-least-once handling not accepted |

## Constraints, Options, And Tradeoffs

Asynchronous delivery decouples signer requests from consumers, but introduces duplicate, delayed, reordered and terminal-failure handling. Consumers can own deduplication by event UUID, while an organization adapter can add inbox/outbox reconciliation and durable schema versioning.

## Impacts And Boundaries

Webhooks affect revenue-critical onboarding state and must not be treated as exactly once or as the authoritative evidence record. See the [data/job diagram](../diagrams/data-job-artifact-provenance.md).

## Change, Reversal, And Follow-Up

OI-005 must close schema, authenticity, retry/order/replay, retention and support semantics with vendor evidence and consumer tests.

