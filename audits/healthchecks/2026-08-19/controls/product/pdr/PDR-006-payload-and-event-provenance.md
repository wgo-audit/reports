# PDR-006: Payload And Event Provenance

- Status: observed
- Evidence cutoff: 2026-08-19

## Decision Statement

Ping events retain arrival metadata, kind, optional exit status/run ID, and a bounded
request body; `/log` records an event without changing state. The default body limit is
10,000 bytes, with optional object storage for larger stored bodies.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Product behavior/promise | Users can inspect or download retained diagnostic bodies; full logs belong in a log system. | [E-018](../../../evidence/evidence-ledger.md#E-018) | Hosted retention/visibility unknown. |
| Implementation | Ingestion truncates, persists, and may externally store/retrieve the body; pruning removes old records. | [E-005](../../../evidence/evidence-ledger.md#E-005), [E-018](../../../evidence/evidence-ledger.md#E-018) | Recovery and actual contents unknown. |
| Runtime/demonstration | unknown | [OI-009](../../open-items.md#OI-009) | No payload was submitted. |
| Approval/specialist sign-off | unknown | [OI-004](../../open-items.md#OI-004) | No data classification/security approval. |

## Constraints, Options, And Tradeoffs

Payloads improve diagnosis but increase privacy, retention, storage, and notification
exposure. Event receipt proves only that a request reached Healthchecks.

## Impacts And Boundaries

Pull/make allow Acme-controlled retention/storage; buy transfers visibility to the
vendor boundary. Neither option makes payload text authoritative business evidence.

## Change, Reversal, And Follow-Up

Default critical pings to no body or a small non-sensitive summary. Route hosted data
approval through OI-004 and job-specific payload classification through OI-009.
