# Product Decision Register

## Records

| ID | Statement | Domain | Status | Evidence confidence | Record link |
|---|---|---|---|---|---|
| PDR-001 | Events API acceptance is not durable storage confirmation. | Event ingestion | observed | High for source/promise; low for live loss envelope | [record](pdr/PDR-001-accepted-event-is-not-durable-event.md) |
| PDR-002 | A single configurable tracker source serves multiple distribution and legacy variants. | Tracker | observed | High for source; runtime coverage unknown | [record](pdr/PDR-002-single-source-configurable-tracker.md) |
| PDR-003 | Dashboard and public API share statistics semantics and surface bounded-output warnings. | Statistics | observed | High for source/docs; live correctness unknown | [record](pdr/PDR-003-shared-stats-query-semantics.md) |
| PDR-004 | Conversion analysis layers goals, revenue, funnels, and bounded journeys. | Product analysis | observed | High for source/docs | [record](pdr/PDR-004-layered-conversion-analysis.md) |
| PDR-005 | Team/site roles, shared links, and SSO are observed as distinct access layers; approval and tenant operation are unknown. | Access | observed | High for source/docs; tenant operation unknown | [record](pdr/PDR-005-layered-access-and-sso-governance.md) |
| PDR-006 | Versioned plans and centralized feature/quota gates govern commercial access. | Subscription | observed | High for source; customer/runtime reconciliation unknown | [record](pdr/PDR-006-versioned-commercial-entitlements.md) |
| PDR-007 | Imported analytics is bounded aggregate history with explicit query limitations. | Imports | observed | High for source/docs | [record](pdr/PDR-007-bounded-imported-data-semantics.md) |
| PDR-008 | Aggregate dashboard export and queued native export are separate product modes. | Exports | observed | High for visible modes; live completion unknown | [record](pdr/PDR-008-distinct-aggregate-and-native-export-modes.md) |
| PDR-009 | Visitor identity is derived from transient request data while customer event inputs remain a separate privacy boundary. | Privacy/data | observed | High for source; legal/control effectiveness unknown | [record](pdr/PDR-009-derived-identity-and-customer-input-boundary.md) |
| PDR-010 | Cloud and CE visibly differ in operational responsibility and premium capability; formal approval is unknown. | Edition boundary | observed | High for monorepo/public description; CE runtime unknown | [record](pdr/PDR-010-cloud-community-edition-product-boundary.md) |

## Coverage And Disposition

| Domain | Candidates | Records | Other dispositions | Limitation |
|---|---:|---:|---|---|
| Tracker and event ingestion | 2 | 2 | none | Live delivery/variant coverage remains open. |
| Dashboard, APIs, integrations, analysis | 3 | 2 | 1 deferred | Ecosystem integrations were not individually traced. |
| Subscription and entitlement | 1 | 1 | none | Customer-specific plan/Paddle truth remains open. |
| Teams, sharing, and SSO | 1 | 1 | none | No tenant/IdP demonstration. |
| Imports and exports | 3 | 2 | 1 blocked | Scheduled raw delivery remains outside visible implementation. |
| Privacy and data behavior | 1 | 1 | none | Privacy/legal sign-off and live data inventory are unknown. |
| Cloud and Community Edition | 1 | 1 | none | Separate CE repository is outside scope. |
