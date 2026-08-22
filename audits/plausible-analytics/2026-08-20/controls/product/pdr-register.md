# Product Decision Register

## Records

| ID | Statement | Domain | Status | Evidence confidence | Record link |
|---|---|---|---|---|---|
| PDR-001 | Event collection accepts configurable pageview/custom-event payloads but 202 is not proof of recorded data. | Workflow/input contract | observed | High source; no live round trip | [record](pdr/PDR-001-event-collection-contract.md) |
| PDR-002 | Conversion reporting depends on explicit site-level goal configuration. | Configuration/output semantics | observed | High source; acceptance unknown | [record](pdr/PDR-002-explicit-goal-configuration.md) |
| PDR-003 | Ordered funnel/path analysis is edition-bounded and unavailable in CE source. | Edition/public promise | observed | High source/documentation; requirement unresolved | [record](pdr/PDR-003-edition-bounded-journey-analysis.md) |
| PDR-004 | Trends and report data are delivered through dashboard queries, CSV, and Stats API. | Output/provenance | observed | High source; correctness unverified | [record](pdr/PDR-004-trend-and-export-outputs.md) |
| PDR-005 | Membership roles separate dashboard viewing from measurement/settings administration. | Identity/governance | observed | High source; live assignments unknown | [record](pdr/PDR-005-role-based-dashboard-access.md) |
| PDR-006 | Public and shared-link modes bypass account membership for selected dashboard access. | Identity/governance | observed | High source; live enablement unknown | [record](pdr/PDR-006-alternate-dashboard-sharing.md) |
| PDR-007 | Monthly email is a fixed prior-month summary distributed to configured recipients. | Reporting lifecycle/output | observed | High source; delivery unverified | [record](pdr/PDR-007-monthly-email-summary.md) |

## Coverage And Disposition

| Domain | Candidates | Records | Other dispositions | Limitation |
|---|---:|---:|---|---|
| Maturity/operator acceptance | 2 | 0 | 2 blocked/deferred | No golden-path observation or acceptance record; [OI-006](../open-items.md#oi-006). |
| Users/workflows/lifecycle | 4 | 4 | 0 | Deployed configuration unknown. |
| Outputs/provenance | 2 | 2 | 0 | No reconciled library outputs. |
| Identity/governance | 3 | 2 | 1 merged | Actual roles and sharing state unknown. |
| External dependencies | 1 | 0 | 1 merged | Live ownership/health unknown. |
| Public promises/edition | 2 | 1 | 1 merged | Hosted entitlement and library acceptance unknown. |
| Specialist sign-off | 1 | 0 | 1 deferred | Downstream specialist review required. |
