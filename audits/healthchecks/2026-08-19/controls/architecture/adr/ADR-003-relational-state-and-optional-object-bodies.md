# ADR-003: Relational State With Optional External Ping Bodies

- Status: observed
- Evidence cutoff: 2026-08-19

## Decision Statement

The relational database is authoritative for accounts, projects, checks,
signals, state transitions, channels, and notification history. If S3-compatible
storage is configured, ping bodies larger than 100 bytes are stored as external
objects while the database retains metadata and object size; pruning spans both
stores.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Implementation | Database engines are configurable; object storage is optional; large bodies upload after the database transaction and are deleted through cross-store pruning. | [E-005](../../../evidence/evidence-ledger.md#E-005) | Source does not prove configured engines, object presence, or consistency. |
| Runtime/live state | unknown | [OI-001](../../open-items.md#OI-001), [OI-007](../../open-items.md#OI-007) | No Acme payload classification, live database, bucket, backup, or restore evidence was approved. |
| Rationale | Source comments separate potentially slow object upload from the database transaction and use object storage for larger bodies. | `HC-CODE-001:hc/api/models.py:557-568`; `HC-CODE-001:hc/lib/s3.py:149-158` | Product, cost, and risk rationale is not documented in the reviewed source. |
| Approval | unknown | [audit brief](../../../audit-brief.md) | Acme has not approved payload capture or a storage boundary. |

## Constraints, Options, And Tradeoffs

- Keeping small bodies in the database simplifies retrieval but makes payload
  retention part of database backup, access, and growth decisions.
- External objects reduce database body storage but introduce a second
  consistency, credential, retention, availability, and recovery boundary.
- Object upload occurs after the database transaction. A database row may state
  that an object exists before upload succeeds; notification retrieval waits once
  and then suppresses body retrieval errors.
- Repository guidance says disabling object storage makes already external
  bodies inaccessible and provides no reverse migration.

## Impacts And Boundaries

The deployment must classify whether ping bodies are required at all. Avoiding
payloads can materially reduce privacy, recovery, and cross-store risk. If bodies
are retained, self-hosting requires coordinated database/object backup and
restore; hosted use requires vendor data-boundary review.

## Change, Reversal, And Follow-Up

Use OI-001 to classify payloads and OI-007 to test recovery. Security and Privacy
must evaluate secrets and payload exposure. Do not enable or disable object
storage in production without a migration and rollback plan that accounts for
existing objects.
