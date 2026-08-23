# Recovery And Operations Evidence Packet

## Scope And Evidence Boundary

- Reader question: Which source-visible mechanisms support recovery, job/report continuity, deletion, and detection, and where does effectiveness remain unknown?
- Evidence cutoff: 2026-08-20 at onboarding start, America/Toronto.
- Approved sources and actions: `primary-code` commit `9cc669b97ece3ecd37fcb3950791cb3873d7944d`; read-only source inspection and one bounded evidence collector.
- Exclusions and sensitivity: no library or hosted runtime, backup, restore, alert, account, traffic, incident, or staff evidence; no dependency installation, product test, restore, load test, or system change.

## Observations

| Observation | Source type and exact locator | Observed/effective time | What it establishes | Limitation |
|---|---|---|---|---|
| PostgreSQL and ClickHouse have separate application/query/ingest/deletion roles. | `primary-code:config/runtime.exs:490-723`; `primary-code:lib/plausible/application.ex:33-47` | Commit 2026-08-19; inspected 2026-08-21 | Recovery must cover both authorities and their connections. | Topology, versions, storage, replication, and backup are unknown. |
| Health endpoints query both stores and critical caches; session readiness means transfer was attempted, not successful. | `primary-code:lib/plausible_web/controllers/api/system_controller.ex:21-92`; `primary-code:lib/plausible/session/transfer.ex:81-89` | Same | Source-visible readiness detection exists. | No external probe, alert, or successful takeover evidence. |
| In-memory buffers flush by timer/size and on orderly termination; optional session takeover supports rolling replacement. | `primary-code:lib/plausible/ingestion/write_buffer.ex:20-115`; `primary-code:lib/plausible/session/transfer.ex:1-89,125-186` | Same | Graceful restart mechanisms exist. | Abrupt loss and accepted-versus-stored reconciliation are untested. |
| Oban persists work in PostgreSQL, rescues orphaned jobs after 120 minutes, and can be fully disabled with `DISABLE_CRON`. | `primary-code:config/runtime.exs:322-323,819-913` | Same | Source defines queue/scheduler recovery mechanisms. | Live enablement, backlog, alerting, ownership, and suitability are unknown. |
| Monthly/weekly report jobs permit one attempt; mail errors are caught and ignored by the worker. | `primary-code:lib/workers/send_email_report.ex:1-54`; `primary-code:lib/plausible/mailer.ex:1-21` | Same | A delivery failure can be logged without failing the Oban job. | No missed library report is claimed. |
| CE site removal records pending ClickHouse work, but the reviewed self-host cron does not schedule its cleanup worker. | `primary-code:lib/plausible/site/removal.ex:1-42`; `primary-code:lib/workers/clickhouse_clean_sites.ex:1-153`; `primary-code:config/runtime.exs:819-913` | Same | Edition-specific source scheduling differs. | External CE deployment automation is outside scope. |
| Up-migration is interwoven, but rollback is per-repo and reviewed migration history includes an irreversible, possibly non-atomic ClickHouse change. | `primary-code:lib/plausible_release.ex:26-177,263-283`; `primary-code:priv/ingest_repo/migrations/20240222082911_sessions_v2_versioned_collapsing_merge_tree.exs:1-12`; `primary-code:lib/plausible/data_migration/versioned_sessions.ex:56-78` | Same | Source provides commands but not a universal rollback guarantee. | Deployment ordering, backups, restore, and exercised rollback are unknown. |

## Material Unknowns And Access Limits

No approved evidence establishes database backup coverage, RPO/RTO, restore success, alert delivery, queue/report health, accountable operators, or hosted internal control operation. Documented outside audited scope; not independently verified: the separate CE deployment repository may define additional operational controls.

## Reuse Guidance

Use [E-035](../evidence-ledger.md#e-035) through [E-038](../evidence-ledger.md#e-038) for reconciled evidence. Do not treat this packet, a source mechanism, a health endpoint, a rollback command, or a vendor statement as proof of live recovery.
