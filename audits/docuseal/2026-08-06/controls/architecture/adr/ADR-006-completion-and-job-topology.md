# ADR-006: Completion And Job Topology

- Status: observed
- Evidence cutoff: 2026-08-06

## Decision Statement

Signer completion commits SQL evidence and then enqueues Sidekiq processing that generates artifacts and triggers mail/webhooks. In single-tenant defaults, Sidekiq and Redis can be managed inside the Puma lifecycle; SQL, queue and object writes are not one demonstrated atomic transaction.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Implementation | Post-commit enqueue, embedded-capable worker/Redis, lock rows and retries | [Data packet §3–4, §7, §10](../../../evidence/packets/architecture-data-jobs-migrations-provenance.md); [runtime packet §4–5](../../../evidence/packets/architecture-runtime-deployment-delivery-identity-secrets.md) | Exactly-once/reconciliation unproved |
| Runtime/live state | unknown | No queue, job or replica telemetry | Durability, drain and backlog unknown |
| Rationale | unknown | No topology record found | Default convenience is not production rationale |
| Approval | unknown | No target operations acceptance | Failure semantics not accepted |

## Constraints, Options, And Tradeoffs

Embedded defaults minimize services but couple failure/scaling. Production options include external Redis and isolated workers, explicit outbox/inbox reconciliation, idempotent stages, stale-lock/orphan cleanup and bounded retry/dead-letter handling.

## Impacts And Boundaries

Lost or duplicated handoffs can affect signed outputs and onboarding completion. Database connection budgets depend on Puma and Sidekiq concurrency.

## Change, Reversal, And Follow-Up

OI-003 must validate isolated topology, capacity, failure/restart/replay and reconciliation. Business Continuity and Scalability must not infer reliability from source retry code.
