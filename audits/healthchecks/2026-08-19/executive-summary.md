# Executive Summary

## Mandate, Boundary, And Bottom Line

Acme asked whether to pull and self-host upstream Healthchecks, make and maintain
a fork, or buy Healthchecks.io for a core operational dependency. The required
outcome is an actionable alert to a responsible human within five minutes of a
critical job missing expected completion, with monitoring-service RTO 30 minutes
and RPO 5 minutes.

**Bottom line:** compare **buy and pull through parallel, time-bounded due
diligence**. Buy has a published recurring product price and, by operating model,
can transfer some runtime duties; pull preserves control and source availability
while assigning production, recovery, security, notification, and upgrade duties
to Acme. The available evidence does not establish an all-in burden ranking.
Consider **make only if a demonstrated requirement needs source divergence**;
otherwise a fork adds stewardship without solving a known need.

This is not a go-live approval. A buy decision requires vendor/security review,
cloud-data minimization, account/exit continuity, plan fit, and end-to-end alert
proof. A pull decision requires a target topology, accountable ownership,
recovery/security design, and equivalent alert proof. The source and public
evidence cutoff is 2026-08-19; no Acme runtime or team evidence was available,
and that absence is neutral about team capability.

The audit-work API-equivalent cost closeout is [Final](controls/cost-estimate.md)
at `$103.02` displayed (`$103.0189036` exact). This API-equivalent audit-execution
estimate is separate from, and does not change, the product-option cost conclusion.

## Current Product And Control Position

Healthchecks is a credible passive dead-man's-switch product. It supports
schedule/grace rules, start/success/failure/exit-status signals, run IDs,
bounded event payloads, and multiple notification integrations. It does not
prove that a job produced the correct business result, and its Windows evidence
is limited to generic HTTP examples rather than an operational Task Scheduler
contract.

The source quality signal is strong but bounded: 22,750 hosted test executions
passed at the pinned commit, strict mypy and three CodeQL jobs passed, and the
project has a long public history and release path. Those are upstream inputs,
not Acme acceptance or production reliability.

The most important control gap is the alert chain. A flip is marked processed
before asynchronous channel delivery completes; the reviewed path does not put
a failed delivery back into a durable retry state. The default alert worker
count is one, channels for a flip run sequentially, generic HTTP can consume
three 30-second attempts, and a due-check calculation failure can defer a check
for one hour. The built-in container health check tests HTTP and the database,
not alert-worker or human-delivery health. An independent Acme-controlled
watchdog and secondary route are mandatory for every option.

### Business Concern Conclusions

| Concern | Supported conclusion |
|---|---|
| `acme-pull-make-buy` | Completed: buy and pull require parallel bounded due diligence; make requires a demonstrated source-change need; no production option is yet approved. |
| `select-sustainable-option` | Partial: the evidence does not support an all-in burden ranking between buy and pull; selection depends on vendor terms, target topology, alert proof, ownership, plan fit, and exit requirements. |
| `five-minute-critical-alert` | Not proven for any option. T0-to-actionable-human tests must pass within 300 seconds with no silent loss. |
| `silent-monitor-failure` | Source-level silent-loss and worker-health risks exist; recommendation requires an independent watchdog and route. |
| `unsustainable-ownership` | Pull assigns more infrastructure duties to Acme; buy retains material integration, vendor, account, alert, and exit duties. Their sustainable burden requires measured, Acme-specific evidence. Make adds fork stewardship if source divergence is required. |
| `team-readiness-unknown` | Unknown by design. Required roles and skills are defined, but no conclusion about team ability is made. |
| `workload-growth-envelope` | Fewer than 100 jobs is not a capacity proof. Cadence, bursts, fan-out, bodies, retention, and growth are unknown. |
| `job-monitoring-fit` | Strong fit for known-schedule heartbeat monitoring; incomplete for business-outcome correctness, overlapping non-latest runs, and Windows operations. |
| `pull-make-buy-risk` | Pull concentrates operating/recovery risk at Acme; make adds fork risk; buy concentrates vendor/account/data risk. All require independent alert proof. |
| `maintenance-love` | Exact hours and an all-in burden ranking are unsupported. Measure option-specific routine and surge work before selection; a fork adds upstream-merge and release duties if chosen. |
| `option-cost` | Buy list price is known; no option has a verified all-in TCO or lowest-cost ranking. Infrastructure rates and measured opportunity time are absent. |
| `hosted-cloud-visibility` | Potentially controllable through no-body pings, opaque names, scoped relays, and review, but not yet accepted or contractually verified. |
| `payload-data-exposure` | Material across DB, backups, optional object storage, providers, and hosted processors. Send no body by default and approve any exception. |
| `identity-access-security` | Useful Argon2, WebAuthn/TOTP, roles, and rate limits exist; bearer ping capabilities, proxy trust, member privileges, credential storage, and supply-chain acceptance require controls. |
| `capacity-retention-footprint` | Mechanisms are understood, but CPU, RAM, storage, request-rate, burst, and queue headroom are unproven; preliminary sizing is unsupported. |
| `upstream-continuity` | BSD-3-Clause and active public history preserve an exit path, but source and hosted operation are concentrated and Acme has no named successor plan. |
| `assessment-absence-guard` | Satisfied after calibration: normally private or Acme-specific unknowns are neutral unless a decision requires them; direct source findings remain separate. |

## Material Risks, Unknowns, And Decisions

### Decision-Useful Conclusions

1. **Do not rank buy and pull before Acme-specific evidence exists.** Run the
   smallest useful vendor/security review and self-host feasibility exercise in
   parallel. Compare the same alert, recovery, ownership, exit, and cost outcomes
   rather than favoring the option with more public documentation.
2. **Do not create a fork without a source-change requirement.** This is a scope
   decision, not a high-severity finding. Reconsider [OI-017](controls/open-items.md)
   only if buy and pull cannot meet a demonstrated requirement without a code
   divergence that Acme is prepared to steward.
3. **Treat the five-minute outcome as Acme-owned for all options — High severity,
   Medium scope.** Product state and “Sent”/“Delivered” stop before responsible-
   human receipt. The smallest move is the OI-006 fault suite with an independent
   watchdog and independently controlled escalation path.
4. **The 100-job hosted boundary is a commercial step, not comfortable headroom.**
   Business is capped at 100 jobs; Business Plus is four times its published
   subscription price. The smallest move is an exact critical-check and
   one-year-growth map with alert-credit reserve under OI-015.
5. **Do not budget the preliminary self-host figures.** The proposed resource,
   setup-day, and monthly-hour numbers have no production-shaped evidence.
   Measure opportunity time through a pilot; do not monetize it without an
   approved conversion rate.

### Decisions Now

Canonical details and closure routes are in the [open-items register](controls/open-items.md).

- OI-015: choose the hosted plan and billing cadence only after check/growth and alert-credit mapping.
- OI-005: approve a production topology only if pull becomes the selected track; never adopt the sample Compose topology unchanged.
- OI-017: select make only if a narrow source change and 36-month stewardship charter are explicitly approved.

OI-013 is already fixed: RTO is 30 minutes and RPO is 5 minutes. It now constrains
vendor terms, self-host design, recovery testing, and cost.

### Evidence Needed

- OI-004, OI-006, OI-009, OI-012, OI-014, OI-015, OI-016, OI-018, and OI-021:
  establish hosted acceptability, five-minute/no-loss behavior, per-job
  contracts, account continuity, capacity, plan fit, successor readiness,
  measured opportunity time, and customer-impact mapping.
- OI-001 and OI-002: validate the minimum job inventory and accountable skill
  coverage without broad team interviews. Unknown capability is not a negative
  team assessment.
- OI-003: apply actual supplier rates after topology/plan selection; keep
  engineering effort as opportunity time over 36 months.

### Implementation Corrections

- Common: OI-011, OI-016, OI-019, OI-020, OI-022, and OI-023 — capability/data
  lifecycle, successor coverage, operating model, claim control, change
  authority, and learning trace.
- Pull only if selected: OI-007, OI-008, and OI-010 — recovery/rollback,
  immutable promotion, and production hardening.

## Evidence-Supported 30–90 Day Plan

| Timing | Accountable owner | Action | Evidence basis | Exit evidence |
|---|---|---|---|---|
| Days 0–15 | CTO | Name service owner, technical approver, security/vendor owner, billing owner, primary and deputy; require a demonstrated source-change need before considering make. | OI-012, OI-016, OI-017, OI-022 | Signed role/authority record and explicit fork-selection condition |
| Days 0–20 | Service owner with bounded job owners | Map only the critical job set: expected completion, business outcome, grace, overlap, payload class, responder, and customer-impact tier. | OI-001, OI-009, OI-021 | Reviewed per-job contracts and prioritized critical-check count |
| Days 10–30 | Security/vendor owner | Complete hosted review; define no-body pings, opaque names/tags, scoped relay credentials, retention/deletion, identity, incident, availability, export, and exit requirements. | OI-004, OI-011 | Approved vendor/data decision or documented buy rejection |
| Days 10–30 | Platform/reliability owner | Define one credible pull topology and estimate the smallest production-shaped pilot using Acme's actual platform, ownership, recovery, and security constraints. | OI-002, OI-005, OI-007, OI-010, OI-018 | Feasibility record with named owners, topology, pilot scope, and explicit rejection reasons if pull is not viable |
| Days 20–45 | Service and billing owners | Select Business or Business Plus using one-year check growth and synchronized alert-credit demand; establish primary/deputy billing controls. | OI-015 | Plan decision, quota reserve, renewal and loss-of-owner evidence |
| Days 25–60 | Reliability owner | Run comparable non-production acceptance tests for each still-viable buy or pull candidate across success, explicit failure, missed completion, degradation, burst, quota exhaustion, recovery, and independent escalation. | OI-006, OI-009, OI-014, OI-018 | Comparable alert, recovery, capacity, and measured-effort evidence for each viable candidate |
| Days 45–75 | Service owner and continuity owner | Exercise account loss, export/recreation, vendor unavailability, secondary alerting, and recovery/exit against RTO 30 minutes and RPO 5 minutes. | OI-012, OI-013, OI-016 | Measured recovery/exit evidence and named stop/fallback authority |
| Days 60–90 | CTO and technical approver | Decide: approve buy or pull with conditions, or stop the initiative. Consider make only if the evidence identifies a necessary source divergence and the stewardship charter is accepted. | OI-004 through OI-019 as applicable | Recorded OI-022 decision with comparable evidence, rationale, residual risk, rollback/exit point, and next review |

## Reader Routing And Limits

The [Product Manager Notes](product-manager-notes.md) govern capability and
promise boundaries. The [Technical Lead Notes](technical-lead-notes.md) govern
architecture and acceptance. Detailed specialist evidence is in
[reviewer reports](reviewer-reports/); canonical work remains in
[open items](controls/open-items.md).

The audit did not inspect Acme systems, team ability, contracts, job schedules,
payloads, provider rates, or live Healthchecks.io internals. It did not deploy,
load-test, or run a customer workflow. Revenue magnitude, incident probability,
precise self-host spend, and sustainable hours are unknown.
