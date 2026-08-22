# Product Decision Candidate Inventory

## Source Boundary

This inventory covers `primary-code` at commit `9cc669b97ece3ecd37fcb3950791cb3873d7944d`, cutoff-effective repository history, and separately labelled post-cutoff validation from `PUBLIC-WEB-001`. It does not establish the library's deployed version, live configuration, hosted entitlement, customer acceptance, or specialist sign-off. A golden-path observation was unavailable because no approved safe environment, identity, and fixture existed.

## Coverage Domains

| Domain | Evidence boundary | Candidate count | Limitation/closure |
|---|---|---:|---|
| Maturity and demonstration | Source, changelog, and public CI boundaries | 1 | Runtime demonstration and library acceptance require [OI-006](../open-items.md#oi-006). |
| Users and workflows | Tracker/API, dashboard, goals, reports, roles, sharing | 7 | Library workflow configuration is unknown. |
| Lifecycle and configuration/persistence | Event receipt, goal setup, PostgreSQL configuration, ClickHouse analytics | 3 | Deployed state and end-to-end reconciliation require [OI-001](../open-items.md#oi-001) and [OI-006](../open-items.md#oi-006). |
| Outputs and provenance | Dashboard, CSV, Stats API, monthly email | 2 | Output acceptance and mail/API operation are unverified. |
| Identity and governance | Team/site roles, public/shared access, email recipients | 3 | Actual role matrix and sharing settings are unverified. |
| Specialist sign-off | No legal/privacy/security acceptance evidence | 1 | Downstream specialist review; no product approval inferred. |
| External dependencies | Website integration, mail, API keys, PostgreSQL/ClickHouse | 2 | Enabled dependencies and ownership are unknown. |
| Public promises | README and post-cutoff public documentation | 2 | Hosted promises are not live-service proof. |
| Operator/admin acceptance | No approved configured environment or acceptance record | 1 | [OI-006](../open-items.md#oi-006). |

## Decision Candidates

| Candidate ID | Decision or durable behavior | Domain | Evidence | Observed/approved status | Disposition | Record or closure |
|---|---|---|---|---|---|---|
| PROD-DC-001 | Browser tracker or Events API accepts pageview/custom-event payloads with optional properties; some drops can still receive HTTP 202 and are signalled by a response header. | Workflow/input contract | [E-016](../../evidence/evidence-ledger.md#e-016), [E-020](../../evidence/evidence-ledger.md#e-020), [E-004](../../evidence/evidence-ledger.md#e-004) | observed; live behavior and approval unknown | record-created | [PDR-001](pdr/PDR-001-event-collection-contract.md) |
| PROD-DC-002 | Received events become named conversions only after a site-level page, event, or scroll goal is configured; goal reports expose visitors, events, and conversion rate. | Configuration/output semantics | [E-017](../../evidence/evidence-ledger.md#e-017) | observed; library metric acceptance unknown | record-created | [PDR-002](pdr/PDR-002-explicit-goal-configuration.md) |
| PROD-DC-003 | CE supports discrete goals and behavioral filters, while ordered funnels and user-journey exploration are EE-only and publicly listed as unavailable in CE. | Edition/public promise | [E-015](../../evidence/evidence-ledger.md#e-015), [E-017](../../evidence/evidence-ledger.md#e-017) | observed/documented; library requirement unresolved | record-created | [PDR-003](pdr/PDR-003-edition-bounded-journey-analysis.md); [OI-007](../open-items.md#oi-007) |
| PROD-DC-004 | Dashboard queries support historical/realtime periods, custom dates, comparisons, filters, breakdowns, and goal metrics; results can be exported through dashboard CSV or authenticated Stats API. | Output/provenance | [E-017](../../evidence/evidence-ledger.md#e-017), [E-019](../../evidence/evidence-ledger.md#e-019), [E-022](../../evidence/evidence-ledger.md#e-022) | observed; output correctness and acceptance unknown | record-created | [PDR-004](pdr/PDR-004-trend-and-export-outputs.md) |
| PROD-DC-005 | Team and site memberships define owner/admin/editor/viewer/billing and guest access; viewer paths reach dashboards and editor-or-higher paths reach measurement settings. | Identity/governance | [E-018](../../evidence/evidence-ledger.md#e-018), [E-021](../../evidence/evidence-ledger.md#e-021) | observed/documented; assignments and approval unknown | record-created | [PDR-005](pdr/PDR-005-role-based-dashboard-access.md) |
| PROD-DC-006 | Dashboard access can also be opened through a public-site setting or unique shared link, optionally password-protected and segment-limited, without membership. | Identity/governance | [E-018](../../evidence/evidence-ledger.md#e-018), [E-021](../../evidence/evidence-ledger.md#e-021) | observed/documented; live enablement unknown | record-created | [PDR-006](pdr/PDR-006-alternate-dashboard-sharing.md) |
| PROD-DC-007 | Monthly email is a scheduled prior-calendar-month summary with fixed metrics/top-five lists, arbitrary configured recipients, and one worker attempt. | Reporting lifecycle/output | [E-019](../../evidence/evidence-ledger.md#e-019), [E-022](../../evidence/evidence-ledger.md#e-022) | observed/documented; delivery and acceptance unknown | record-created | [PDR-007](pdr/PDR-007-monthly-email-summary.md) |
| PROD-DC-008 | CE removes application site/member limits, while hosted limits and feature access are plan-driven. | Configuration/commercial boundary | [E-015](../../evidence/evidence-ledger.md#e-015), [E-018](../../evidence/evidence-ledger.md#e-018) | observed for source; hosted entitlement unknown | merged-into | PDR-003 and PDR-005 cover the decision-changing edition/access boundaries; Expense Exposure must validate hosted plan entitlement. |
| PROD-DC-009 | The end-to-end library workflow has no approved runtime demonstration or acceptance record. | Maturity/operator acceptance | [E-010](../../evidence/evidence-ledger.md#e-010), [E-013](../../evidence/evidence-ledger.md#e-013) | unknown | blocked | [OI-006](../open-items.md#oi-006); do not substitute EE-only E2E or source presence. |
| PROD-DC-010 | Website integration, mail delivery, API keys, PostgreSQL, and ClickHouse are external product dependencies. | External dependencies | [E-003](../../evidence/evidence-ledger.md#e-003), [E-006](../../evidence/evidence-ledger.md#e-006), [E-016](../../evidence/evidence-ledger.md#e-016), [E-019](../../evidence/evidence-ledger.md#e-019) | observed interfaces; live ownership/health unknown | merged-into | PDR-001, PDR-004, and PDR-007; operational proof remains in [OI-001](../open-items.md#oi-001) and [OI-006](../open-items.md#oi-006). |
| PROD-DC-011 | Privacy, security, legal, and records-governance acceptance are not established by product source or public promises. | Specialist sign-off | [E-015](../../evidence/evidence-ledger.md#e-015) | unknown | deferred | Security and Privacy reviewer; no legal conclusion is made here. |
