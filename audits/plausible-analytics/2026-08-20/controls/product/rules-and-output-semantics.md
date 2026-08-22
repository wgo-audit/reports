# Rules And Output Semantics

## Evidence Boundary

These are source-observed rules at the approved commit, not live results or accepted library definitions. See [E-016](../../evidence/evidence-ledger.md#e-016) through [E-019](../../evidence/evidence-ledger.md#e-019).

| Rule or output | Source-bounded meaning | Library consequence | Unknown / closure |
|---|---|---|---|
| Event name | `pageview` is special; other names are custom events. Tracker may ignore localhost, automated-browser, excluded-path, local-storage opt-out, or falsy transformed payloads. | Instrumentation design must standardize names and avoid unintentionally suppressed events. | Installed settings and representative receipt: [OI-006](../open-items.md#oi-006). |
| HTTP response | Validation failures may return 400; other dropped events can return 202 with `x-plausible-dropped`; buffered events also return 202. | A client callback/status alone cannot prove a stored measurement. | Failure/reconciliation: [OI-003](../open-items.md#oi-003). |
| Properties | Request parsing retains at most 30 properties and validates key/value length; a goal may constrain up to three custom properties. | Search/registration dimensions must fit these contracts and avoid visitor-identifying content. | Accepted data dictionary and privacy review: [OI-006](../open-items.md#oi-006) plus Security and Privacy. |
| Goal | A received custom event is not automatically a named conversion; an editor-or-higher configures a page, event, or scroll goal. | Goal setup is part of implementation, not merely reporting. | Representative configuration/output: [OI-006](../open-items.md#oi-006). |
| Conversion output | Goal breakdown exposes unique converting visitors, total events/conversions, and conversion rate; precise interpretation depends on configured filters/date range. | Monthly trends can answer service-find/use questions only after definitions are accepted. | Metric acceptance and reconciliation: [OI-006](../open-items.md#oi-006). |
| Journey | CE exposes discrete goals and session behavioral filters, but ordered funnels and path exploration are EE-only. | Run is partial if ordered step/drop-off analysis is required. | Acceptance decision: [OI-007](../open-items.md#oi-007). |
| Trend | Dashboard supports realtime, day/month, rolling periods, custom ranges, and previous-period/year-over-year/custom comparison. | Monthly and seasonal trend questions are expressible. | Performance/correctness at assumed scale belongs to Scalability and [OI-006](../open-items.md#oi-006). |
| Monthly email | Prior calendar month in site timezone; fixed overall metrics and top-five pages, sources, and goals; one send attempt. | Useful summary, but not a configurable formal report or delivery guarantee. | Mail proof and adequacy: [OI-006](../open-items.md#oi-006); continuity tolerance [OI-002](../open-items.md#oi-002). |
| Access | Viewer/guest viewer can see assigned dashboards; editor can alter site measurement/settings; admin/owner manage broader access. Public/shared-link and email-recipient paths are separate. | "Role-restricted dashboard" is supported, but optional sharing and email distribution need explicit governance. | Role/share/recipient matrix: [OI-006](../open-items.md#oi-006). |
| CSV/API | Dashboard export follows current date/filter/goal context; Stats API provides JSON queries; source exposes CE routes, while hosted entitlement is plan-specific. | Reusable monthly reporting is possible outside the fixed email. | API key, entitlement, and output reconciliation: [OI-006](../open-items.md#oi-006). |
