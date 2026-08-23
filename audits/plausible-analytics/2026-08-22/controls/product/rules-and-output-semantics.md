# Product Rules And Output Semantics

## Evidence Boundary

Rules below come from the pinned public source and approved public documentation. They describe visible contracts, not production correctness or customer acceptance.

## Evidence Dimensions Used

Implementation and documented promise are present. Runtime demonstration, customer-specific entitlement, commercial acceptance, and specialist/legal approval are unknown.

## Current Source-Bounded Position

| Rule/output | Input/control | Visible result | Material qualification | Evidence |
|---|---|---|---|---|
| Event acceptance | Parsed request enters ingestion and filtering | Controller returns HTTP `202`; buffered path returns text `ok` | Some filtered events also return `202` with a drop header; durability is later | [E-021](../../evidence/evidence-ledger.md#e-021), [OI-001](../open-items.md#oi-001) |
| Event validation | Invalid payload/site/request | HTTP `400` JSON error | Public example shows `{}` for success while source/tests expect `ok` | [E-021](../../evidence/evidence-ledger.md#e-021), [OI-012](../open-items.md#oi-012) |
| Unique visitor derivation | Salt + user agent + remote IP + domain/root domain (+ replay ID) | Derived `user_id`; geo/device attributes derived from transient inputs | Source loads current and previous salts; retention wording needs reconciliation | [E-027](../../evidence/evidence-ledger.md#e-027), [OI-011](../open-items.md#oi-011) |
| Customer event data | URL/referrer, custom properties, revenue payload | Valid bounded values may be stored as event attributes | Privacy outcome depends on integration choices; no evidence personal data is actually supplied | [E-027](../../evidence/evidence-ledger.md#e-027), [OI-011](../open-items.md#oi-011) |
| Revenue | Revenue payload plus matching configured goal/currency | Revenue retained and may be converted | Without a matching revenue goal, the event can remain while revenue is discarded | [E-023](../../evidence/evidence-ledger.md#e-023) |
| Goals | Page/event/scroll goal, up to three custom properties | Goal becomes an analysis dimension | Reserved system names and site cap apply; revenue is cloud feature-gated | [E-023](../../evidence/evidence-ledger.md#e-023) |
| Funnels | Ordered goal steps | Sequential or strict-order funnel output | At least two steps; tier gated | [E-023](../../evidence/evidence-ledger.md#e-023) |
| Journeys | Selected page/event step and direction | Next/back path exploration | Maximum 20 steps and rate limits | [E-023](../../evidence/evidence-ledger.md#e-023) |
| Stats query | Metrics, dimensions, filters, date range, imports/comparison flags | Results plus query/meta | Imported data/revenue/comparison can produce warnings or skip reasons; v1 invalid-page defect is open | [E-022](../../evidence/evidence-ledger.md#e-022), [OI-007](../open-items.md#oi-007) |
| Subscription usage | Total pageviews plus custom events across team | Usage/limit state | Sustained overage across two cycles plus margin/grace precedes dashboard lock; collection/settings behavior is documented | [E-025](../../evidence/evidence-ledger.md#e-025) |
| Feature access | Plan generation, feature module, team limits, enterprise overrides | Allowed, unavailable, or `upgrade_required` | Public plan copy is not customer-specific runtime truth | [E-025](../../evidence/evidence-ledger.md#e-025), [OI-009](../open-items.md#oi-009) |
| SSO | Enterprise feature, SAML/JIT policy, force option, session timeout | Team access follows IdP and role policy | Default viewer; 30-minute–12-hour timeout; force mode excludes owners | [E-024](../../evidence/evidence-ledger.md#e-024) |
| Historical imports | GA/CSV aggregates | Imported series can be included with native results | Five-complete-import cap and missing dimensions/metrics; full native export excludes imported data. Separately, the pinned CE cleanup misclassification can purge completed imports. | [E-026](../../evidence/evidence-ledger.md#e-026), [E-016](../../evidence/evidence-ledger.md#e-016), [OI-006](../open-items.md#oi-006) |
| Dashboard export | Selected report/query | CSV/ZIP aggregate output | Quick export row/property caps apply | [E-026](../../evidence/evidence-ledger.md#e-026) |
| Full export | Queued site native-data request | S3/local archive and completion communication | Execution/retrieval/security not observed; distinct from scheduled raw export | [E-026](../../evidence/evidence-ledger.md#e-026), [OI-014](../open-items.md#oi-014) |

## Material Unknowns And Closure Routes

The material open contracts are event durability ([OI-001](../open-items.md#oi-001)), complete plan/edition/variant truth ([OI-009](../open-items.md#oi-009)), scheduled raw export ([OI-010](../open-items.md#oi-010)), and privacy-copy/salt reconciliation ([OI-011](../open-items.md#oi-011)).
