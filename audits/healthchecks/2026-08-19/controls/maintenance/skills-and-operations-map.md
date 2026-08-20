# Skills And Operations Map

Reader question: Which capabilities and recurring controls must remain covered for each option without inferring Acme team ability or headcount?

## Evidence Boundary

This map derives required capabilities from [E-046](../../evidence/evidence-ledger.md#E-046), [E-049](../../evidence/evidence-ledger.md#E-049), the [quality control](../quality/test-health-and-change-safety.md), and the [continuity controls](../continuity/expiry-and-maintenance-control.md). Team identity, proficiency, availability, on-call coverage, and contracting options were intentionally not assessed. A capability can be combined in one person or supplied externally only after Acme verifies coverage; the table is not a staffing-count recommendation.

## Capability Coverage

| Capability | Pull | Make | Buy | Evidence of safe coverage required |
|---|---|---|---|---|
| Service/reliability ownership | Primary and deputy own SLOs, job contracts, five-minute path, incidents, capacity, and maintenance calendar. | Same. | Same, including vendor escalation and service-change review. | Named primary/deputy; OI-006, OI-014, OI-016, OI-019 exercises. |
| Linux/container/network/TLS operations | Required for runtime, reverse proxy, DNS/TLS, process supervision, observability, and host/platform lifecycle. | Same as pull. | Not required for vendor runtime; still needed for Acme job connectivity and independent watchdog where applicable. | Deployed-control review, expiry tests, and incident rehearsal. |
| Database/storage/recovery | Required for backup, point-in-time target, restore, migration, rollback, cleanup, retention, and optional object-store reconciliation. | Same after upstream merges and fork releases. | Vendor evidence plus Acme export, reconstruction, and cutover capability. | OI-007 and OI-013 measured RTO/RPO evidence. |
| Release and test engineering | Pin/review upstream releases; execute upstream plus Acme job, fault, capacity, migration, and browser gates. | Same plus merge/conflict, fork-diff, build/provenance, release, and compatibility ownership. | Revalidate contracts, integrations, quotas, and exit after material service change. | OI-008 promotion evidence; make also OI-017. |
| Python/Django application maintenance | Needed for source triage and emergency diagnosis; a pull should avoid local product changes. | Deep capability required for custom design, upstream integration, migrations, security fixes, and test maintenance. | Not required for hosted runtime; source literacy remains useful for exit/self-host fallback but is not proven necessary for routine buy operation. | Demonstrated safe-change/rebuild exercise; no individual is presumed capable. |
| Security/IAM/secret lifecycle | Hardening, proxy trust, dependency advisories, keys, integration secrets, privileged access, and offboarding. | Same plus fork vulnerability triage/remediation and artifact provenance. | Vendor/security review, minimized data, account MFA/access, capability URLs, processor/terms change, and offboarding. | OI-004, OI-010, OI-011, and OI-012. |
| Notification/on-call integration | Provider credentials, quotas, independent route, human escalation/acknowledgement, and failure drills. | Same. | Same Acme-owned destination/response work; vendor owns sender runtime only within verified boundaries. | OI-006 and OI-015 tests. |
| Job-platform integration | Unix/Windows wrappers, schedules/timezones, retries, overlap policy, business-outcome signal, endpoint rotation. | Same. | Same. | OI-009 golden paths for every critical job class. |
| Vendor/commercial/exit control | Upstream release/security channel and infrastructure/provider contracts. | Same plus upstream relationship and fork-succession policy. | Hosted security/terms/support, billing, plan/quota, export, escalation, and exit. | OI-004, OI-012, OI-015, and OI-016. |

## Operating Trigger And Cadence Map

| Trigger/cadence | Pull | Make | Buy | Retained outcome evidence |
|---|---|---|---|---|
| Continuous | Runtime/worker/database/resource/TLS reachability and independent ping-to-human watchdog. | Same. | External service and independent route; account/plan health where observable. | Alerts, acknowledgement, aged-work/queue metrics, and tested escalation. |
| Per release or material service change | Advisory and changelog review; immutable candidate; acceptance/migration/rollback decision. | Same plus merge/conflict/custom-diff and artifact publication. | Terms/security/API/integration/quota review and targeted regression/exit check. | Version/change decision, gate results, rollback/cutover result. |
| Scheduled | Backup verification, cleanup/retention, certificate/credential expiry, capacity trend, access/billing review. | Same plus fork backlog and upstream divergence review. | Account/billing/access/quota, vendor evidence, data/export and exit-copy review. | Completed checks, exceptions, owner and next due date. |
| Exercise | Five-minute fault path, 30-minute recovery, 5-minute data-loss bound, loss-of-owner/successor, and provider failure. | Same after material fork change. | Five-minute path, vendor outage/account loss, export/rebuild/cutover, successor. | Measured T0/T1, RTO/RPO, restored/reconstructed service, and action log. |
| Incident/emergency patch | Diagnose, contain, recover, patch/promote, and verify. | Same plus source fix/rebase/release duty. | Escalate vendor, operate independent path, validate recovery, and trigger exit if thresholds are exceeded. | Timeline, decision, evidence, follow-up, and opportunity time. |

## Material Unknowns And Closure Routes

Acme skill coverage and availability remain unknown by design; this map must not be used to label the team capable or incapable. OI-002 requires coverage comparison, OI-016 requires primary/deputy succession, OI-018 measures time, and OI-019 converts the map into an approved operating model.
