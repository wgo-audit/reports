# Product Capability Contract Matrix

## Evidence Boundary

This source-bounded view reconciles public product/docs claims with pinned implementation at `9cc669b97ece3ecd37fcb3950791cb3873d7944d`. It does not establish deployment, customer acceptance, entitlement fulfillment, output correctness, pricing validity for a customer, or legal sign-off.

## Evidence Dimensions Used

Implementation and public promise/documentation are present. Targeted public history is present where linked in [provenance notes](provenance-notes.md). Live operation, customer acceptance, ownership/approval, customer-specific commercial terms, and specialist evidence are unknown.

## Current Source-Bounded Position

| Capability/workflow | Public promise or contract | Visible mechanism/control | Output/acceptance boundary | Position | Evidence/closure |
|---|---|---|---|---|---|
| Browser tracker and Events API | Privacy-oriented browser, server, and mobile event collection | Configurable tracker posts JSON to `/api/event`; ingestion validates, enriches, filters, and buffers | `202` can include policy-dropped events and is not ClickHouse durability | Aligned with material boundary; response example conflicts with visible `ok` body | [E-020](../../evidence/evidence-ledger.md#e-020), [E-021](../../evidence/evidence-ledger.md#e-021), [OI-001](../open-items.md#oi-001), [OI-012](../open-items.md#oi-012) |
| Dashboard statistics | Real-time audience/content/acquisition and behavioral analysis | Typed dashboard query client, controller/parser, ClickHouse query runner | Imported/revenue/comparison warnings and skip reasons affect meaning | Aligned in source; no live golden path | [E-022](../../evidence/evidence-ledger.md#e-022), [OI-008](../open-items.md#oi-008) |
| Public Stats API | Business-tier v2 query endpoint with documented metrics, dimensions, filters, rate limits | API authorization/scopes/feature gates; shared query construction and result shape | Query/table heuristics and imported-data constraints can change results; invalid v1 `page` path remains open | Broad alignment; one known API validation defect | [E-022](../../evidence/evidence-ledger.md#e-022), [E-017](../../evidence/evidence-ledger.md#e-017), [OI-007](../open-items.md#oi-007) |
| Goals/custom events | Page, event, scroll, property and revenue goals | Typed goals, caps, reserved names, property bounds, revenue-goal matching | Revenue is retained only for a matching goal; invalid revenue need not reject the event | Aligned with documented semantics | [E-023](../../evidence/evidence-ledger.md#e-023) |
| Funnels and journeys | Business-tier sequential/strict funnels and next/back user journeys | Funnel validation/order and exploration controls | Funnels require 2+ steps; journeys are bounded to 20 steps and rate limited | Aligned in source; live result correctness unknown | [E-023](../../evidence/evidence-ledger.md#e-023) |
| Imports | GA/CSV historical import with stated limitations | Import UI/workers and imported-data query flags | Maximum five completed imports; aggregates omit some native dimensions/metrics | Aligned and candidly documented; destructive CE cleanup defect remains open | [E-026](../../evidence/evidence-ledger.md#e-026), [E-016](../../evidence/evidence-ledger.md#e-016), [OI-006](../open-items.md#oi-006) |
| Aggregate/native exports | Quick CSV/ZIP and full native data export | Dashboard export caps plus queued S3/local full export workers | Quick reports have row/property caps; full export excludes imported aggregates | Aligned in visible source; live completion unknown | [E-026](../../evidence/evidence-ledger.md#e-026), [OI-014](../open-items.md#oi-014) |
| Scheduled raw event exports | Configured Enterprise delivery to S3/GCS on agreed cadence | No delivery implementation established in approved monorepo | Not real-time or self-serve; schema, destination security, SLO, and acceptance unknown | Public promise only | [E-029](../../evidence/evidence-ledger.md#e-029), [OI-010](../open-items.md#oi-010) |
| Teams and sharing | Role-based teams, guest/site access, password/segment-limited shared links | Membership roles, policy checks, shared-link settings | Public links require no account; permissions differ by team/site role | Aligned in source; tenant negative paths unobserved | [E-024](../../evidence/evidence-ledger.md#e-024), [OI-013](../open-items.md#oi-013) |
| SSO | Enterprise SAML, JIT, session policy, force-SSO controls | Feature-gated SSO settings, owner/admin control, 2FA and timeout policies | Owners retain emergency access; tenant/IdP operation unobserved | Detailed alignment; no live demonstration | [E-024](../../evidence/evidence-ledger.md#e-024), [OI-013](../open-items.md#oi-013) |
| Subscription/usage | Starter/Growth/Business/Enterprise capability ladder and usage grace | Versioned plan files, benefit strings, feature modules, quota lock logic | Usage combines pageviews/custom events; sustained two-cycle overage plus grace can lock dashboard | Public ladder broadly aligns; customer-specific truth unresolved | [E-025](../../evidence/evidence-ledger.md#e-025), [OI-009](../open-items.md#oi-009) |
| Privacy/data behavior | No stored raw IP/UA; day/site/device-scoped derived visitor identity | IP/UA used transiently for geo/device/hash; current/previous salt; customer properties accepted | Data-policy says salt deleted every 24h while source deletes rows older than 48h; customer inputs affect data classification | Partial corroboration; copy/control reconciliation required | [E-027](../../evidence/evidence-ledger.md#e-027), [OI-011](../open-items.md#oi-011) |
| Cloud versus CE | Managed operations/frequent releases/premium features in Cloud; operator responsibility and LTS in CE | Compile-time CE/EE paths and feature exclusions in one monorepo | CE packaging/release operation is outside approved corpus | Source/public story align within boundary | [E-028](../../evidence/evidence-ledger.md#e-028), [OI-004](../open-items.md#oi-004) |

## Material Unknowns And Closure Routes

- Reconcile plan generation, runtime feature decisions, Paddle/custom terms, documentation, and a sample of grandfathered tenants under [OI-009](../open-items.md#oi-009).
- Obtain the scheduled raw-export service/runbook/schema and a completed customer delivery under [OI-010](../open-items.md#oi-010).
- Resolve privacy-copy and salt-lifecycle semantics with privacy/legal and engineering owners under [OI-011](../open-items.md#oi-011).
- Demonstrate access-control and queued native-export outcomes under [OI-013](../open-items.md#oi-013) and [OI-014](../open-items.md#oi-014); these are distinct from the scheduled raw-export promise.
- Demonstrate one authorized tracker-to-ingest-to-dashboard path plus tier-negative cases under [OI-008](../open-items.md#oi-008); none was run in this audit.
