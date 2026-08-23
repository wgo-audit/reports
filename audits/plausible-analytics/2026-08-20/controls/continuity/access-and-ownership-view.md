# Access And Ownership Continuity View

Reader question: Can control be transferred if a staff member, account, or service owner disappears?

## Evidence Boundary

Source-visible application roles, transfer mechanisms, configuration keys, and cutoff-effective public hosted documentation were reviewed. No library user/account inventory, identity-provider record, secret value, infrastructure account, contract, or handoff exercise was available.

## Evidence Dimensions Used

Implementation and public product/terms evidence are present. Effective ownership, approval, access review, successor readiness, and operating custody are unknown.

## Current Source-Bounded Position

| Control surface | Source/documented mechanism | Ownership state | Continuity consequence | Closure |
|---|---|---|---|---|
| Dashboard/team/site | Owner/admin/editor/viewer/billing/guest roles; sole owner cannot leave; ownership/site transfer paths exist. | Library assignments and number of owners are unknown. | Loss of a sole usable owner can block access changes and transfer even though source prevents voluntary abandonment. | [OI-008](../open-items.md#oi-008), [OI-015](../open-items.md#oi-015) |
| Super-admin/recovery account | `ADMIN_USER_IDS` can identify application super-admins. | Enabled IDs, authentication protection, use, and successor are unknown. | An unowned or stale privileged path can either prevent recovery or widen access risk. | [OI-001](../open-items.md#oi-001), [OI-015](../open-items.md#oi-015) |
| Deployment/registry/DNS/edge | Image workflow and runtime configuration exist. | Library GitHub/container-registry, compute, DNS/CDN, ingress, and promotion owners are unknown. | Run may not be patchable, restartable, or transferable when one operator/account disappears. | [OI-001](../open-items.md#oi-001), [OI-005](../open-items.md#oi-005), [OI-015](../open-items.md#oi-015) |
| PostgreSQL/ClickHouse/backups | Separate datastore roles are source-visible. | Administrative accounts, encryption keys, backup operators, restore authority, and successors are unknown. | Data recovery and deletion can fail even when application access remains. | [OI-004](../open-items.md#oi-004), [OI-015](../open-items.md#oi-015) |
| Mail/telemetry/geolocation/S3/secrets | Optional external services and secret-file/environment injection exist. | Enabled set, service accounts, rotation, ownership, and replacements are unknown. | Reports, alerts, exports, or startup can fail independently. | [OI-001](../open-items.md#oi-001), [OI-014](../open-items.md#oi-014), [OI-015](../open-items.md#oi-015) |
| Hosted subscription/billing/support | Public docs describe account ownership transfer; terms assign account security to the customer and provide reasonable-effort email support. | Library account/billing owner, procurement authority, support contacts, and successors are unknown. | Subscribe transfers infrastructure operation but not account, renewal, escalation, export, or termination accountability. | [OI-015](../open-items.md#oi-015) |

Evidence: [E-006](../../evidence/evidence-ledger.md#e-006), [E-018](../../evidence/evidence-ledger.md#e-018), [E-025](../../evidence/evidence-ledger.md#e-025), [E-027](../../evidence/evidence-ledger.md#e-027), [E-039](../../evidence/evidence-ledger.md#e-039).

## Material Unknowns And Closure Routes

[OI-015](../open-items.md#oi-015) requires a primary-and-successor responsibility matrix and bounded handoff/export exercise. It must not record secrets; redacted account identifiers, control domains, role owners, and tested recovery routes are sufficient.
