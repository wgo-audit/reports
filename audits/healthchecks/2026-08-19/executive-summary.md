# Executive Summary

## Mandate, Boundary, And Bottom Line

Acme asked whether to pull and self-host upstream Healthchecks, make and maintain
a fork, or buy Healthchecks.io for a core operational dependency. The required
outcome is an actionable alert to a responsible human within five minutes of a
critical job missing expected completion, with monitoring-service RTO 30 minutes
and RPO 5 minutes.

**Bottom line:** run a time-bounded **buy-first acceptance track**, keep **pull as
the fallback and exit path**, and **do not make**. Buy has the only published
recurring product price and the lowest evidenced Acme runtime/source-maintenance
burden. Pull preserves control and source availability but transfers the full
production, recovery, security, notification, and upgrade burden to Acme. Make
adds permanent fork stewardship without an evidenced product, security,
reliability, scale, or revenue benefit.

This is not a go-live approval. Buy remains stopped by vendor/security review,
cloud-data minimization, account/exit continuity, plan fit, and end-to-end alert
proof. If those gates fail, Acme should test pull against the same outcome and
recovery contract. The source and public evidence cutoff is 2026-08-19; no Acme
runtime or team evidence was available.

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
| `acme-pull-make-buy` | Completed: buy-first proof, pull fallback, make stopped; no production option is yet approved. |
| `select-sustainable-option` | Partial: buy is the least maintenance-intensive candidate, but vendor, alert, ownership, and exit gates remain open. |
| `five-minute-critical-alert` | Not proven for any option. T0-to-actionable-human tests must pass within 300 seconds with no silent loss. |
| `silent-monitor-failure` | Source-level silent-loss and worker-health risks exist; recommendation requires an independent watchdog and route. |
| `unsustainable-ownership` | Pull has high initial and material recurring opportunity-time burden; make is strictly no lower and is stopped; buy retains material Acme control work. |
| `team-readiness-unknown` | Unknown by design. Required roles and skills are defined, but no conclusion about team ability is made. |
| `workload-growth-envelope` | Fewer than 100 jobs is not a capacity proof. Cadence, bursts, fan-out, bodies, retention, and growth are unknown. |
| `job-monitoring-fit` | Strong fit for known-schedule heartbeat monitoring; incomplete for business-outcome correctness, overlapping non-latest runs, and Windows operations. |
| `pull-make-buy-risk` | Pull concentrates operating/recovery risk at Acme; make adds fork risk; buy concentrates vendor/account/data risk. All require independent alert proof. |
| `maintenance-love` | Exact hours are unsupported. Relative burden is buy lower, pull high initial/material recurring, make highest and unbounded. |
| `option-cost` | Buy list price is known; no option has a verified all-in TCO or lowest-cost ranking. Infrastructure rates and measured opportunity time are absent. |
| `hosted-cloud-visibility` | Potentially controllable through no-body pings, opaque names, scoped relays, and review, but not yet accepted or contractually verified. |
| `payload-data-exposure` | Material across DB, backups, optional object storage, providers, and hosted processors. Send no body by default and approve any exception. |
| `identity-access-security` | Useful Argon2, WebAuthn/TOTP, roles, and rate limits exist; bearer ping capabilities, proxy trust, member privileges, credential storage, and supply-chain acceptance require controls. |
| `capacity-retention-footprint` | Mechanisms are understood, but CPU, RAM, storage, request-rate, burst, and queue headroom are unproven; preliminary sizing is unsupported. |
| `upstream-continuity` | BSD-3-Clause and active public history preserve an exit path, but source and hosted operation are concentrated and Acme has no named successor plan. |
| `assessment-absence-guard` | Satisfied: every missing Acme, hosted, workload, team, and runtime fact is retained as an explicit unknown or verification gate. |

## Material Risks, Unknowns, And Decisions

### Decision-Useful Conclusions

1. **Reject make now — High severity, Large remediation scope.** No reviewer
   found a source-level benefit that offsets fork ownership. The smallest move
   is to keep [OI-017](controls/open-items.md) as a stop condition and reconsider
   only after a pull/buy acceptance test isolates a defect that external controls
   cannot close.
2. **Prefer buy for the first acceptance track — conditional, not approved.**
   It offers the lowest evidenced operating burden and a clear list-price
   baseline, but public terms provide no Acme SLA and the vendor describes a
   one-person company. The smallest move is the bounded vendor/security review
   in OI-004 plus no-body/opaque-name data minimization.
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
- OI-017: keep make stopped unless a narrow source change and 36-month stewardship charter are explicitly approved.

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
| Days 0–15 | CTO | Name service owner, technical approver, security/vendor owner, billing owner, primary and deputy; keep make stopped. | OI-012, OI-016, OI-017, OI-022 | Signed role/authority record and explicit make stop condition |
| Days 0–20 | Service owner with bounded job owners | Map only the critical job set: expected completion, business outcome, grace, overlap, payload class, responder, and customer-impact tier. | OI-001, OI-009, OI-021 | Reviewed per-job contracts and prioritized critical-check count |
| Days 10–30 | Security/vendor owner | Complete hosted review; define no-body pings, opaque names/tags, scoped relay credentials, retention/deletion, identity, incident, availability, export, and exit requirements. | OI-004, OI-011 | Approved vendor/data decision or documented buy rejection |
| Days 20–45 | Service and billing owners | Select Business or Business Plus using one-year check growth and synchronized alert-credit demand; establish primary/deputy billing controls. | OI-015 | Plan decision, quota reserve, renewal and loss-of-owner evidence |
| Days 25–60 | Reliability owner | Run a non-production hosted pilot across success, explicit failure, missed completion, worker/provider-equivalent degradation, burst, quota exhaustion, and independent escalation. | OI-006, OI-009, OI-014 | Retained T0/T1 results at or below 300 seconds with no silent loss |
| Days 45–75 | Service owner and continuity owner | Exercise account loss, export/recreation, vendor unavailability, secondary alerting, and recovery/exit against RTO 30 minutes and RPO 5 minutes. | OI-012, OI-013, OI-016 | Measured recovery/exit evidence and named stop/fallback authority |
| Days 60–90 | CTO and technical approver | Decide: approve buy with conditions, reject it and start a pull pilot, or stop the initiative. If pull starts, require target topology, hardening, immutable promotion, restore/rollback, capacity, and the same alert tests. | OI-004 through OI-019 as applicable | Recorded OI-022 decision with rationale, residual risk, rollback/exit point, and next review |

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
