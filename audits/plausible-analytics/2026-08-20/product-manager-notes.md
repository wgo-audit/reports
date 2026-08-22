# Product Manager Notes

## Capability, Workflow, And Promise Position

Plausible's assessed source supports the library's baseline service-measurement needs: pageviews and named custom events with properties; explicit page, event, and scroll goals; visitors, events, and conversion rates; historical/realtime trends and comparisons; filters and breakdowns; dashboard CSV; authenticated Stats API; a fixed prior-month email summary; and owner/admin/editor/viewer/billing plus guest access paths. The [capability matrix](controls/product/capability-contract-matrix.md) and [PDR register](controls/product/pdr-register.md) trace these claims.

The fit is conditional in three important ways:

1. CE can represent search and registration as separate stages and conversion rates, but ordered funnels and user-journey exploration are EE-only. [OI-007](controls/open-items.md#oi-007) determines whether this is a gap.
2. The built-in monthly email is a fixed summary, not a customizable formal report or delivery guarantee. A governed dashboard/CSV/API reporting process may be needed, with visible failure handling under [OI-014](controls/open-items.md#oi-014).
3. Source presence is not acceptance. [OI-006](controls/open-items.md#oi-006) requires one synthetic, non-production search/registration round trip across submission, goals, output reconciliation, email, and representative roles.

## Decisions And Specialist Sign-Off Boundaries

| Option | Product promise that can be made now | Approval boundary |
|---|---|---|
| Run | “The assessed CE source is functionally plausible for aggregate trends, discrete search/registration stages, goals, exports, monthly summaries, and role-separated dashboards.” | Do not promise ordered funnel/path analysis, durable completeness, live role correctness, report delivery, peak dependability, or privacy/security readiness until OI-002/OI-006–OI-008/OI-014/OI-019 close. |
| Subscribe | “Hosted Plausible may add vendor operation and edition-bounded journey capabilities.” | Do not promise entitlement, one-team fit, capacity, controls, SLA/support, price, or lower total burden until the accepted topology, quote, assurance, functional proof, owners, and exit route close OI-006–OI-008/OI-015/OI-017–OI-020. |
| Replace | “The audit supplies a reusable privacy-first requirements envelope for a later shortlist.” | No current product, price, migration, control, support, capacity, or maintenance comparison exists. Do not start a full selection this fiscal year unless the approved journey or control requirements make both Plausible options unacceptable. |

Privacy/records and security authorities own the event/data/access/retention contract, not the product team alone. IT/continuity owns recovery and loss/outage evidence. Procurement owns the hosted entitlement, control, support, renewal, and exit proof. Qualified counsel must assess applicable legal obligations separately.

## Material Gaps, Risks, And Next Work

- Define a minimal event dictionary for one search and one registration journey. Prohibit search text, form content, visitor identifiers, and unnecessary URL/query data; specify redaction, retention, deletion, recipients, roles, keys, and sharing through [OI-008](controls/open-items.md#oi-008).
- Decide whether separately reported stages satisfy this year's decision need. If ordered drop-off/path analysis is mandatory, validate hosted entitlement or define a bounded external-reporting requirement; do not label stage counts as an ordered journey.
- Define the monthly decision artifact: fixed email, governed dashboard export, CSV/API report, or a reconciled combination. Include recipient control, data meaning, failure detection, and an owner.
- Use synthetic events and test identities only for acceptance. Reconcile submitted, stored, and reported results; include an error path and negative role/alternate-access checks without viewing live visitor traffic.
- Size hosted quota from pageviews **plus custom events by month**, not annual pageviews alone. The assumed 14 million annual pageviews average 1,166,666.67/month before events and do not describe seasonal peaks.
- Treat 18 properties and 25 staff as an access/reporting topology question, not just a traffic tier. One Business team is publicly limited to 10 sites and 10 members; Enterprise or a separately billed multi-team design requires validation.

## Evidence And Limits

The [Product Value report](reviewer-reports/product-value/report.md) provides the detailed source trace. [Security and Privacy](reviewer-reports/security-privacy/report.md), [Application Security](reviewer-reports/application-security/report.md), [Expense Exposure](reviewer-reports/expense-exposure/report.md), and [Scalability](reviewer-reports/scalability/report.md) own their respective approval boundaries.

The assessed commit is not the library's deployed version. No golden path, live role assignment, visitor traffic, hosted entitlement, non-public service, or replacement candidate was inspected. HTTP 202 is not proof that an event became durable or reportable. The reconciled [audit-and-operationalization cost estimate](controls/cost-estimate.md) is **$87.24 USD** on an API-equivalent token basis, not a Codex invoice; the [public receipt](controls/cost-calculation.json) preserves the exact calculation and the [audit-only receipt](controls/cost-calculation-audit-only.json) remains unchanged.
