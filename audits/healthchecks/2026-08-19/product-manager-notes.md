# Product Manager Notes

The audit-work API-equivalent cost closeout is [Final](controls/cost-estimate.md)
at `$103.02` displayed; it is separate from the pull/make/buy commercial and
opportunity-cost analysis.

## Capability, Workflow, And Promise Position

Healthchecks is a strong fit for passive monitoring of periodic jobs whose
expected completion can be described. The pinned product supports simple,
Cron, and calendar schedules; grace; start/success/failure/exit-status signals;
run IDs; pauses; bounded diagnostic events; and multi-channel routing. It is not
active uptime monitoring, application-performance monitoring, or log
aggregation.

A heartbeat proves only that the configured signal arrived. It does not prove
that a customer-facing business outcome completed correctly. Overlapping runs
receive display correlation through run IDs, but alert timing follows the most
recent start, so a hung non-latest run can escape duration alerting. Windows
support is protocol-compatible but lacks an audited Task Scheduler operating
contract.

Allowed wording today is: “Healthchecks implements passive schedule/failure
monitoring and invokes configured notification integrations.” Do not say that a
job is “protected,” that an alert was delivered to a human, or that the service
meets the five-minute, RTO, or RPO target. UI “Sent” and “Delivered” represent
transport completion without an application-level error, not acknowledgement.

## Decisions And Specialist Sign-Off Boundaries

| Decision | Product/service sign-off | Required specialist sign-off |
|---|---|---|
| Critical job is ready | Per-job schedule/timezone, outcome assertion, grace, overlap policy, payload class, responder, and customer-impact tier | Reliability owner validates start/success/fail/missing and human-receipt cases; security approves data/capability handling |
| Buy pilot | Minimum hosted metadata and exact plan/check mapping | Security/vendor review, billing/account continuity, reliability T0/T1 test, exit/recovery proof |
| Pull fallback | Same job contract and user workflow as buy | Platform topology, security hardening, quality/promotion, capacity, backup/restore/rollback, independent watchdog |
| Make exception | A failed acceptance test demonstrates a source-level gap unavailable by configuration or external control | CTO approves OI-017 fork charter, owners, release/merge/security plan, and 36-month opportunity capacity |
| External or executive claim | Exact wording, audience, option/configuration, owner, evidence date, and correction path | Claim owner plus the control owner whose evidence supports the statement |

## Material Gaps, Risks, And Next Work

- Build the initial pilot around a bounded set of critical jobs, not all jobs.
  Each needs a job-monitoring contract and business-outcome assertion.
- Set grace so it preserves enough of the five-minute budget for queueing,
  provider delivery, and escalation. The auto-provisioned one-hour grace is not
  suitable for this mandate.
- Use no request body by default, opaque check names, unique per-job UUIDs, and
  no shared slug auto-provisioning for critical jobs.
- Require at least one independently controlled alert path. A second channel
  inside the same delayed worker/provider chain is not automatically independent.
- Map one-year growth before selecting the hosted plan; “slightly fewer than
  100 jobs” does not establish fewer than 100 production checks.
- Keep customer/revenue impact unknown until OI-021 maps jobs to outcomes,
  commitments, fallbacks, and communications. Do not invent loss estimates.

## Evidence And Limits

Use the [capability matrix](controls/product/capability-contract-matrix.md),
[claim governance](controls/revenue/claim-governance.md), and
[exposure register](controls/revenue/exposure-register.md). The canonical
closure routes are in [open items](controls/open-items.md), especially OI-004,
OI-006, OI-009, OI-011, OI-015, OI-020, and OI-021.

The conclusions are source-bounded. Hosted feature parity, Acme job definitions,
live behavior, human receipt, customer promises, and team readiness were not
observed.
