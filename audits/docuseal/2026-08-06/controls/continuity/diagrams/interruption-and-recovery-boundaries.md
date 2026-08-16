# Interruption And Recovery Boundaries

## Purpose And Evidence Boundary

- Reader question: Where can a signer-completion interruption be detected, recovered, reconciled, and transferred, and which links remain unknown?
- Evidence cutoff: 2026-08-06; Community `3.1.7` / `a2d8b855491793870b7b4acf176d2d95ae95ff83`.
- Confirmed notation: solid nodes/edges are source-visible mechanisms.
- Inferred notation: dotted labelled edges are source-supported interruption consequences, not observed failures.
- Unknown notation: dashed nodes and dotted edges identify missing target, live, ownership, or exercise evidence.
- Evidence links: [recovery packet](../../../evidence/packets/business-continuity-recovery-dataops-alerting.md), [transfer packet](../../../evidence/packets/business-continuity-delivery-account-transfer.md), [Architecture data/job diagram](../../architecture/diagrams/data-job-artifact-provenance.md), and [Security trust diagram](../../security/diagrams/identity-data-trust-boundaries.md).

## Evidence Dimensions Used

Implementation, cutoff-bounded upstream build history, and auditor-approved availability/RPO targets are present. Measurement definitions, observed target operation, recovery exercises, dashboard/alert delivery, execution ownership/approval, cost/commercial evidence, and specialist acceptance are unknown.

## Diagram

```mermaid
flowchart TB
  classDef unknown stroke-dasharray: 5 5,fill:#f7f7f7,color:#555;
  subgraph REQUEST["Confirmed signer request and durable handoff"]
    FORM["Signer completion"] --> SQL["SQL values, events, completion state"]
    SQL --> ENQUEUE["Separate Sidekiq enqueue"]
  end
  subgraph PROCESS["Confirmed asynchronous processing"]
    REDIS["Redis queue and schedules"] --> WORKER["Completion worker"]
    WORKER --> LOCK["SQL lock/retry/fail rows"]
    LOCK --> BLOB["Result, audit, combined blobs"]
  end
  subgraph DELIVERY["Confirmed downstream handoffs"]
    MAIL["Queued SMTP email"]
    WEBHOOK["Webhook attempts and retries"]
  end
  subgraph SIGNALS["Confirmed source signals"]
    UP["Rails /up"]
    LOGS["Structured stdout logs"]
    UI["Sidekiq/webhook admin views"]
    CLIENTERR["Optional browser Rollbar"]
  end
  subgraph UNKNOWN["Unknown target continuity controls"]
    DETECT["Dependency readiness, metrics, alert delivery, on-call"]
    RESTORE["Point-in-time SQL/blob/key restore and Redis recovery"]
    RECON["Orphan, stale lock, schedule and downstream reconciliation"]
    COMMAND["Incident command, safe pause, customer communication, controlled resume"]
    OWNER["Primary/backup owners and access-transfer rehearsal"]
  end
  REQUEST --> PROCESS
  PROCESS --> DELIVERY
  PROCESS --> SIGNALS
  ENQUEUE -. "atomicity unproved" .-> RECON
  BLOB -. "blob/marker alignment unproved" .-> RECON
  REDIS -. "queue/schedule recovery unproved" .-> RESTORE
  DELIVERY -. "terminal-failure response unknown" .-> COMMAND
  SIGNALS -. "alert path unproved" .-> DETECT
  DETECT -. "measurement and authority unknown" .-> COMMAND
  COMMAND -. "restore sequence unknown" .-> RESTORE
  RESTORE -. "integrity/resume proof unknown" .-> RECON
  OWNER -. "control transfer unproved" .-> DETECT
  OWNER -. "access/custody unproved" .-> RESTORE
  class DETECT,RESTORE,RECON,COMMAND,OWNER unknown;
```

## Known Gaps And Follow-Up

- BC-Q-001 is answered: monthly availability targets are 99.5% for signing and 99% for onboarding, maximum data loss/RPO is two hours, and onboarding may pause during interruption. The unknown stages must now be measured and exercised against those targets; synchronous transactions remain a design preference, not an observed guarantee.
- OI-002–OI-006/OI-013 carry recovery, artifact/key, release, contract, and vendor proof. Canonical OI-014/OI-015/OI-016 carry incident response, ownership inventory, and access-transfer proof.
- Solid paths are source-visible behavior, not proof of a completed production workflow. No outage, restoration, failover, alert, incident, or transfer was performed or observed.
- The named `observability-and-response-path.md` was not created because no approved dashboard, alert ownership, incident, or alert-delivery evidence met its explicit trigger; this diagram preserves the unknown boundary without implying operation.
