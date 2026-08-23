# Expiry And Maintenance Control

## Purpose And Evidence Boundary

This source-bounded register identifies time-based dependencies that can stop
monitoring or transfer. It does not assert that Acme has configured, scheduled,
or assigned any control. Evidence:
[E-005](../../evidence/evidence-ledger.md#E-005),
[E-007](../../evidence/evidence-ledger.md#E-007),
[E-022](../../evidence/evidence-ledger.md#E-022),
[E-024](../../evidence/evidence-ledger.md#E-024), and
[E-030](../../evidence/evidence-ledger.md#E-030).

| Time-bound dependency | Interruption consequence | Minimum control | Pull | Make | Buy | Route |
|---|---|---|---|---|---|---|
| TLS certificate, DNS/domain, reverse proxy | Producers or operators cannot reach the service | Managed renewal, expiry alert through an independent path, deputy ownership | Acme | Acme | Vendor for service edge; Acme for producer/network dependencies | OI-005, OI-010, OI-012 |
| Database backup and restore evidence | State/configuration loss or prolonged recovery | Scheduled backup, retention, restore drill, RPO/RTO evidence | Acme | Acme | Vendor plus contractual evidence; Acme exit copy | OI-004, OI-007, OI-013 |
| Object-store lifecycle and credentials | Diagnostic bodies unavailable or stale objects retained | Credential rotation, cross-store backup/reconciliation, prune monitoring | If enabled | If enabled | Vendor contract/data evidence | OI-007, OI-011 |
| Alert worker and cleanup commands | Missed alerts, growing data, stale deletion state | Supervision; aged-work alerts; scheduled, measured cleanup | Acme | Acme | Vendor runtime; Acme verifies outcome | OI-005..OI-007 |
| Integration/provider tokens and quotas | Alert cannot leave the service | Expiry/quota alert, rotation drill, independent provider/route | Acme | Acme | Shared: vendor sender plus Acme destination/account | OI-006, OI-011, OI-012 |
| Application version, base image, dependencies, upstream patches | Unsupported or vulnerable runtime; risky emergency upgrade | Immutable promotion, update cadence, migration rehearsal, rollback | Acme | Acme plus upstream merge | Vendor; Acme tracks contract/service changes | OI-008, OI-010 |
| Owner/MFA recovery and billing instrument | Administrative lockout or service suspension | Primary/deputy, break-glass recovery, renewal alert, transfer drill | Acme | Acme | Acme account/billing plus vendor process | OI-004, OI-012 |

Upstream names many responsibilities but supplies no Acme schedule, owner,
alert, or completed maintenance evidence. A fork adds a permanent upstream
merge and security-release clock; it does not remove any pull responsibility.
