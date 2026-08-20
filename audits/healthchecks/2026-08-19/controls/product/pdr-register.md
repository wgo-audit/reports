# Product Decision Register

## Records

| ID | Statement | Domain | Status | Evidence confidence | Record link |
|---|---|---|---|---|---|
| PDR-001 | Passive schedule and grace govern Late/Down transitions. | Lifecycle/configuration | observed | High for source, no runtime proof | [record](pdr/PDR-001-passive-schedule-and-grace-contract.md) |
| PDR-002 | Explicit endpoint signals encode execution outcomes. | Workflow/lifecycle | observed | High for source, client use unknown | [record](pdr/PDR-002-execution-signal-contract.md) |
| PDR-003 | Run IDs improve duration correlation but not all-run overrun alerting. | Output/lifecycle | observed | High for source/docs | [record](pdr/PDR-003-overlapping-run-correlation-limit.md) |
| PDR-004 | Method/content filters and pause semantics classify or suppress pings. | Rules/configuration | observed | High for source, chosen rules unknown | [record](pdr/PDR-004-ingress-classification-and-pause.md) |
| PDR-005 | State flips route through selected channels, while Acme's five-minute outcome remains unverified. | Output/dependency | observed | High for source; low for live receipt | [record](pdr/PDR-005-alert-routing-and-five-minute-budget.md) |
| PDR-006 | Event metadata and bounded bodies provide diagnostic provenance, not business-outcome proof. | Output/provenance | observed | High for source, data suitability unknown | [record](pdr/PDR-006-payload-and-event-provenance.md) |
| PDR-007 | Auto-provisioning favors availability with permissive defaults and temporary over-limit creation. | Configuration/lifecycle | observed | High for source, production acceptance unknown | [record](pdr/PDR-007-auto-provisioning-defaults.md) |
| PDR-008 | Projects are the boundary for checks, integrations, API keys, and role-based access. | Identity/governance | observed | High for docs/source, Acme mapping unknown | [record](pdr/PDR-008-project-scoped-governance.md) |
| PDR-009 | Windows has protocol/example support, not a production Task Scheduler contract. | Public promise/workflow | observed | High for bounded corpus, live fit unknown | [record](pdr/PDR-009-windows-example-support-boundary.md) |

## Coverage And Disposition

| Domain | Candidates | Records | Other dispositions | Limitation |
|---|---:|---:|---|---|
| Maturity/demo | 2 | 0 | 1 deferred; 1 blocked | No live environment or hosted-runtime evidence. |
| Users/workflows | 3 | 2 | 1 merged | Acme clients are unknown. |
| Lifecycle | 4 | 3 | 1 merged | No job-specific observed execution. |
| Configuration/persistence | 3 | 3 | none | Selected production values unknown. |
| Outputs/provenance | 3 | 3 | none | Correctness and human receipt unproven. |
| Identity/governance | 1 | 1 | none | Acme ownership mapping unknown. |
| External/public promises | 2 | 1 | 1 blocked | Hosted commitments unavailable; Windows guide is minimal. |
| Operator acceptance | 1 | 0 | 1 merged | The 300-second requirement is routed through PDR-005/OI-006. |
