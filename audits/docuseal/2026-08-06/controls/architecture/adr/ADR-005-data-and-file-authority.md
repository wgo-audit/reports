# ADR-005: Data And File Authority

- Status: observed
- Evidence cutoff: 2026-08-06

## Decision Statement

SQL stores workflow, signer, event, configuration and file metadata; Active Storage stores bytes on disk or S3/GCS/Azure selected by configuration. Archive and permanent delete follow different paths, and source shape does not establish a complete cross-store retention/deletion transaction.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Implementation | Relational authority plus configurable blob provider and mixed lifecycle cleanup | [Data packet §1–2, §12](../../../evidence/packets/architecture-data-jobs-migrations-provenance.md) | Orphan outcome is inferred from source; operational cleanup unknown |
| Runtime/live state | unknown | No datastore/object-store/backup evidence | Provider, HA, residency and encryption unknown |
| Rationale | unknown | No data-authority record found | Supported choices are not target selection |
| Approval | unknown | No retention/residency authority decision | Specialist input required |

## Constraints, Options, And Tradeoffs

The public server-requirements guide recommends PostgreSQL for production API/embedding use. Private object storage is a target option supported by source, not a documented recommendation; the organization must decide authoritative records, consistency, backup order, object versioning/lock, migration, legal hold and verified deletion.

## Impacts And Boundaries

Recovery must preserve relational-to-blob references and signing/audit provenance. Adapter differences and partial indexes mean SQLite/MySQL cannot be assumed equivalent to PostgreSQL.

## Change, Reversal, And Follow-Up

OI-003 selects/tests production stores and OI-006 defines retention, deletion, backup/restore and evidence-preservation closure. See the [data/job diagram](../diagrams/data-job-artifact-provenance.md).
