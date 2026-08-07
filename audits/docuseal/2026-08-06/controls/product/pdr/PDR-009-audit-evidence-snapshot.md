# PDR-009: Audit Evidence Snapshot

- Status: observed
- Evidence cutoff: Community source effective 2026-08-03

## Decision Statement

The audit PDF is generated after completion from current relational submission/submitter/event state and document hashes, then optionally signed and stored as an attachment; it is not source-proven as an append-only immutable event record.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Product behavior/promise | Public FAQ describes verifiable history and legal/compliance evidence. | PV-E-005 | Dynamic vendor promise. |
| Implementation | Audit includes actor/event metadata and hashes; event rows are ordinary relational records and no append-only control was found; audit has optional signature. | PV-E-004 | This does not prove rows are modified in operation; regeneration/immutability policy unknown. |
| Runtime/demonstration | unknown | No audit artifact/retention test | Content correctness unobserved. |
| Approval/specialist sign-off | unknown | OI-006 | Evidentiary acceptance absent. |

## Constraints, Options, And Tradeoffs

Generated PDF evidence is human-readable and portable but inherits source-row integrity, timing, retention, and regeneration controls.

## Impacts And Boundaries

Archive, purge, legal hold, restore, and ledger cleanup affect whether the evidence package remains authoritative and reproducible.

## Change, Reversal, And Follow-Up

Define authoritative event/artifact records, immutability/notarization, retention/legal hold, regeneration rules, and restore/purge verification with specialists.
