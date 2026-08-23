# Product Value

## Audit Question, Depth, And Evidence Boundary

This detailed review asks what Healthchecks can demonstrably do for Acme's critical
jobs, where its workflows and outputs stop, and how product capability differs across
pull, make, and buy. The cutoff is 2026-08-19. Evidence is bounded to `HC-CODE-001`
commit `fafac59eeb00cfdc87166242544fa071ecad1723`, repository documentation and tests,
CodeGraph topology, the approved brief, and direct Architecture evidence linked below.
Reusable Product Value evidence is [E-014 through E-019](../../evidence/evidence-ledger.md).

No safe environment, test identity, job fixture, Acme job inventory, Windows host,
configured provider, responder, hosted runtime, or customer acceptance evidence was
available. No golden-path observation was created. Source presence is not treated as
deployed behavior, job correctness, human receipt, approval, or hosted parity.

## Coverage And Material Gaps

The review traced passive heartbeat schedules, grace/state transitions, start/success/
fail/log/exit endpoints, content classification, pause behavior, duration/run IDs,
overlapping runs, notification routing, payload/event provenance, auto-provisioning,
project roles, Windows examples, and option-level capability differences. The
[candidate inventory](../../controls/product/pdr-candidate-inventory.md) covers every
applicable decision-mining domain; the multi-path capability met the deep-review trigger.

Material gaps are routed through [OI-004](../../controls/open-items.md#OI-004) for
hosted service/control proof, [OI-006](../../controls/open-items.md#OI-006) for the
300-second end-to-end outcome, and new [OI-009](../../controls/open-items.md#OI-009)
for per-job and Windows acceptance. OI-001 remains the prerequisite inventory; OI-008
remains the promotion gate.

### Executed Checks

| Working directory | Command/tool | Intended coverage | Result | Dependency/installation state | Bounded conclusion |
|---|---|---|---|---|---|
| `HC-CODE-001:./` | `codegraph status <absolute-root>`; CodeGraph 1.5.0 | Confirm index before product topology inspection | Pass: up to date; 701 files, 7,177 nodes, 19,074 edges | Existing index; no installation | The pinned tree was indexed; behavior is not proven. |
| `HC-CODE-001:./` | CodeGraph `query`/`explore` with `--path <absolute-root>` for `Check.ping`, `get_grace_start`, `duration`, `exitstatus`, and `notify` | Trace entry points, rules, consumers, outputs, and test relationships | Pass: relevant model/view/worker/transport/test relationships returned | Existing index; no installation | The product paths are traceable; execution and correctness are not established. |
| `HC-CODE-001:./` | Source/test inspection only | Confirm schedule, signal, duration, overlap, filter, and notification semantics | Pass as inspection; no runner started | Dependencies absent and installation prohibited, as recorded in E-013 | Test totals for this reviewer: 0 passed, 0 failed, 0 errors, 0 skipped because no test execution was started. Hosted CI evidence remains E-010, not local proof. |
| Audit root | `python3 core:scripts/validate_audit_structure.py <audit-root>` | Validate canonical structure, links, records, and handoff headings | Pass: 0 errors, 0 warnings | Existing Python; no installation | Product Value outputs satisfy the canonical structural validator; conclusions remain evidence-bounded. |

## Key Findings

| Finding | Severity | Effort | Evidence links | Confidence and limitation | Consequence | Taxonomy |
|---|---|---|---|---|---|---|
| The product can represent a missed completion, but grace intentionally delays Down and the worker/provider/human path follows it. Nothing reviewed proves the complete path reaches an actionable human within 300 seconds. | High | M | [E-003](../../evidence/evidence-ledger.md#E-003), [E-014](../../evidence/evidence-ledger.md#E-014), [E-017](../../evidence/evidence-ledger.md#E-017), [PDR-005](../../controls/product/pdr/PDR-005-alert-routing-and-five-minute-budget.md), [OI-006](../../controls/open-items.md#OI-006) | High for source contract; no runtime evidence | Any pull, make, or buy decision made without the T0/T1 proof can fail the core requirement despite a correct Down state. | none |
| Run IDs correctly correlate displayed durations for overlaps, but timeout alerting retains only the most recent start; an older hung concurrent run can escape duration monitoring. | High | M | [E-015](../../evidence/evidence-ledger.md#E-015), [PDR-003](../../controls/product/pdr/PDR-003-overlapping-run-correlation-limit.md) | High for source/docs; applicability depends on unknown Acme overlap | Critical overlapping work may appear well-instrumented while not every run is protected. | none |
| A success ping is a client assertion and can be sent independently of business-output correctness; HTTP 200 can also correspond to an ignored ping under filters/sticky pause. | High | M | [E-015](../../evidence/evidence-ledger.md#E-015), [E-016](../../evidence/evidence-ledger.md#E-016), [rules view](../../controls/product/rules-and-output-semantics.md) | High for semantics; Acme wrappers/configuration unknown | Incorrect wrapper placement or classification can create silent false assurance. | none |
| If used for a critical job, an auto-provisioned check's one-day period and one-hour grace cannot meet the 300-second outcome. | High | S | [E-019](../../evidence/evidence-ledger.md#E-019), [PDR-007](../../controls/product/pdr/PDR-007-auto-provisioning-defaults.md) | High for source/docs; Acme use is unproven | A monitor may exist and receive pings while remaining unapproved and too slow for critical use. | none |
| Windows has source-documented generic PowerShell/C# HTTP examples, but no Task Scheduler failure, service-account, retry, overlap, secret, history, or alert-verification contract. Protocol compatibility is plausible, not demonstrated. | High | M | [E-015](../../evidence/evidence-ledger.md#E-015), [E-019](../../evidence/evidence-ledger.md#E-019), [Windows view](../../controls/product/windows-scheduled-task-fit.md), [OI-009](../../controls/open-items.md#OI-009) | High for bounded source absence; no Windows fixture | Practical Windows protection is not established and could silently signal only success. | none |
| Ping bodies and event metadata add diagnostic context, but payloads are bounded/stored and may enter notifications; they do not prove the business result. | Medium | S | [E-018](../../evidence/evidence-ledger.md#E-018), [PDR-006](../../controls/product/pdr/PDR-006-payload-and-event-provenance.md) | High for source; payload sensitivity/hosted visibility unknown | Sensitive or misleading context can expand exposure without improving detection correctness. | none |

### Promise, Implementation, Demonstration, And Approval

| Capability | Repository/public promise | Implementation observed | Demonstration | Acme approval | Decision consequence |
|---|---|---|---|---|---|
| Schedule/grace | Missing periodic pings become Late then Down after grace. | Simple, Cron, and OnCalendar rules are present. | None. | Only the 300-second outcome is approved; values are not. | Every critical schedule/timezone/grace needs OI-009 and OI-006. |
| Explicit outcomes | Start, success, fail, log, and exit-status signals are documented. | Routes and state transitions are present. | None. | No wrapper approved. | Signal placement and business-result assertion remain gates. |
| Overlapping runs | Run IDs improve duration calculation; docs disclose the latest-run alert limit. | Per-event RID exists; check-level overrun state is singular. | None. | No overlap policy approved. | Concurrent critical jobs need explicit exclusion, separate checks, or other control. |
| Notification routing | Multiple channels and redundancy are documented. | Enabled channels are selected and attempted sequentially with recorded errors. | No provider or human receipt. | T1−T0 ≤300 seconds is approved. | Every option must pass OI-006 fault cases with no silent loss. |
| Windows | Generic PowerShell/C# HTTP examples are documented. | Platform-neutral endpoints exist. | No Windows fixture or Task Scheduler run. | No Windows contract approved. | Protocol fit is plausible; production fit remains OI-009. |
| Buy parity | Repository pages describe the general Healthchecks workflow. | Hosted implementation is not in evidence. | None. | Vendor/security approval absent. | Buy remains blocked by OI-004 and OI-006. |

## Mandate-Relevant Strengths

- Healthchecks directly models the target problem: passive detection of missing
  periodic completions across simple, Cron, and OnCalendar schedules, with explicit
  timezone and configurable grace ([E-014](../../evidence/evidence-ledger.md#E-014)).
- Start, success, fail, exit status, run IDs, and diagnostic events provide several
  ways to distinguish absence, explicit failure, and long execution when wrappers are
  correct ([E-015](../../evidence/evidence-ledger.md#E-015)).
- Multiple project-scoped notification integrations and explicit redundancy guidance
  provide useful routing seams ([E-017](../../evidence/evidence-ledger.md#E-017)); this
  is not delivery proof.
- The approved workload is slightly below 100 jobs. This review establishes no
  capacity, plan-limit, or cost fit. Subject to OI-009, a job may be represented by a
  check ([audit brief](../../audit-brief.md)).

### Decision Insights

1. **Pull is product-capable but not production-proven.** The source supplies the
   needed primitives; the decisive gaps are Acme job contracts and end-to-end receipt,
   not a missing general feature. Wrongly treating feature presence as protection would
   approve silent failure. Smallest next action: OI-009 for job contracts, then OI-006.
2. **Make has no current product-value case.** Overlap and delivery limitations are
   real, but separate checks, scheduler exclusion, resilient topology, and provider
   diversity may close them without source divergence. Smallest proof: demonstrate a
   critical case still fails after those controls before approving a specific fork
   delta. No fork-specific product delta is currently proposed.
3. **Buy cannot be credited with source-backed parity or the five-minute outcome.** It
   may reduce operating burden, but vendor operation, plan limits, data visibility, and
   delivery behavior were not established. Smallest proof: OI-004 plus the same OI-006
   external end-to-end test.
4. **The five-minute target is a budget, not a grace setting.** Setting grace to five
   minutes leaves no time for detection, queueing, provider transit, or escalation.
   Smallest action: assign an explicit sub-budget and test the complete T0/T1 path.

## Selected Outputs

- Required: [PDR candidate inventory](../../controls/product/pdr-candidate-inventory.md)
  and [PDR register](../../controls/product/pdr-register.md).
- Triggered records: [PDR-001](../../controls/product/pdr/PDR-001-passive-schedule-and-grace-contract.md),
  [PDR-002](../../controls/product/pdr/PDR-002-execution-signal-contract.md),
  [PDR-003](../../controls/product/pdr/PDR-003-overlapping-run-correlation-limit.md),
  [PDR-004](../../controls/product/pdr/PDR-004-ingress-classification-and-pause.md),
  [PDR-005](../../controls/product/pdr/PDR-005-alert-routing-and-five-minute-budget.md),
  [PDR-006](../../controls/product/pdr/PDR-006-payload-and-event-provenance.md),
  [PDR-007](../../controls/product/pdr/PDR-007-auto-provisioning-defaults.md),
  [PDR-008](../../controls/product/pdr/PDR-008-project-scoped-governance.md), and
  [PDR-009](../../controls/product/pdr/PDR-009-windows-example-support-boundary.md).
- Triggered deep-review packet: [capability contract matrix](../../controls/product/capability-contract-matrix.md),
  [product-value flow](../../controls/product/diagrams/product-value-flow.md),
  [rules and output semantics](../../controls/product/rules-and-output-semantics.md), and
  [provenance notes](../../controls/product/provenance-notes.md).
- Triggered source-bounded view: [Windows Scheduled Task fit](../../controls/product/windows-scheduled-task-fit.md).

## Material Omissions, Unknowns, And Auditor Questions

No Product Value question is raised to the auditor. The missing matters require proof,
not assertion: job-by-job acceptance and Windows procedure (OI-009), live human receipt
and faults (OI-006), and hosted capability/control evidence (OI-004). Team readiness is
unknown by design and was not evaluated.

**Documented outside audited scope; not independently verified.** Platform HTTP-client
documentation and Runitor are referenced by repository pages. They cannot establish an
Acme production wrapper or third-party suitability. The smallest useful expansion is
the bounded wrapper/fixture evidence already routed through OI-009.

## Reconciliation

This is a fresh Product Value review; no prior findings, PDRs, or Product Value open
items existed. No material conflict was found between source and repository
documentation. Documentation's broad “alert when late” promise is reconciled with the
implementation as state/dispatch behavior, not human-receipt proof. Architecture's
processed-before-delivery finding remains a direct dependency, not replaced by this
report.

No evidence collectors were started: the main reviewer performed the required
CodeGraph topology pass and direct source review. The mandatory `product_value_quality`
worker read the quality rubric, returned one completed terminal outcome, wrote no audit
state, and identified two blockers plus targeted improvements. One revision pass fixed
the diagram evidence labels/handoffs, bounded the option conclusion, added the four-
state reader view, tightened T0/T1 proof, removed the unsupported capacity claim,
conditioned auto-provisioning severity, and normalized Windows wording. No child task
remains running, open, multiply terminated, or ambiguously correlated.

## Bounded Conclusion And Downstream Guidance

Healthchecks has source-backed product primitives for known-schedule jobs, explicit
failures, and durations. It does not yet establish reliable protection or capacity fit:
per-job semantics, overlapping-run policy, Windows operation, auto-provisioned defaults,
and 300-second human receipt remain open. The pinned source is the only directly
evidenced product contract. This does not approve pull: pull and make remain blocked by
OI-005, OI-006, OI-008, and OI-009, while buy remains blocked by OI-004 and OI-006.

Expense Exposure and Scalability may use the capability matrix to price and size the
actual surfaces. Revenue Risk and Business Continuity should use the promise-versus-
proof boundaries. They must not assume a stored success means a correct job, a Down
state means a human received an alert, Windows is production-ready, hosted equals the
repository, or Acme has the required skills.
