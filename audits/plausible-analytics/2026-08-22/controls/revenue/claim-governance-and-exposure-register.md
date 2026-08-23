# Claim Governance And Commercial-Exposure Register

Reader question: Which cutoff-valid public promises could interrupt a demo,
onboarding, renewal, expansion, trust, or customer delivery if their visible
implementation or operating evidence is mistaken?

## Evidence Boundary

This source-bounded register uses approved public product, legal, status, Git,
issue, and pull-request evidence through 2026-08-22 22:08:28 EDT. Source is
anchored to `primary-code` commit
`9cc669b97ece3ecd37fcb3950791cb3873d7944d`. Mutable pages re-read on
2026-08-23 validate cutoff-visible material only. Public positioning is a
Plausible claim, not proof of live delivery, customer acceptance, contract
scope, revenue, or control effectiveness.

No safe demo identity, fixture, or environment was approved in the
[audit brief](../../audit-brief.md), so no golden-path observation was run. No
customer contract, order form, tenant entitlement, billing record, support
record, renewal record, production evidence, or commercial owner was available
in that approved boundary. The current security page's August 2026
expansions have unknown cutoff-effective timing and do not support this
cutoff-bounded assessment. [E-020](../../evidence/evidence-ledger.md#e-020)
[E-025](../../evidence/evidence-ledger.md#e-025)
[E-046](../../evidence/evidence-ledger.md#e-046)

## Evidence Dimensions Used

| Dimension | Position |
|---|---|
| Public promise/contract | Present for plans, APIs, privacy, Cloud/CE responsibility, exports, security, continuity, support, and service limits. |
| Implementation | Present for selected monorepo capabilities and defects at the pinned commit; no scheduled raw-export service was established in the approved monorepo, and private operations were outside the [approved boundary](../../audit-brief.md). |
| History/rationale | Present for specific public issues and PRs that changed Enterprise benefits, plan gates, Events API responses, imports, and recovery-sensitive releases. |
| Observed operation/demonstration | Unknown; no approved golden path or production access. Public status history is provider communication, not an independent service test. |
| Customer-effective commercial state | Unknown; no customer-specific price, contract, order form, entitlement, usage, renewal, acceptance, or support record. |
| Ownership/approval | Unknown for each claim, live control, commercial exception, and correction path. |

## Current Source-Bounded Position

| Exposure route | Evidence type | Promise or customer boundary | Implementation / operating position | Business consequence if assumed incorrectly | Owner or authority unknown | Smallest closure route |
|---|---|---|---|---|---|---|
| Expansion and premium delivery | `[Plausible public claim]` plus `[verified source/history]` | Enterprise includes team-configured scheduled raw-event delivery to S3/GCS and says it is not real-time or self-serve; customer-effective cadence or commitment is unknown. | The exact benefit was added in merged PRs #5574/#5963, but the approved monorepo search established no scheduler, destination delivery, schema/version, or fulfillment service. An internal service may exist outside scope; live completion and customer acceptance are unknown. | Sales or expansion can present a premium capability whose service boundary, security, acceptance, and support path the incoming CTO cannot yet govern. | Product authority, service owner, support owner, commercial approver, and security owner are unknown. | Prove the service and one completed delivery under [OI-010](../open-items.md#oi-010); reconcile customer-effective terms under [OI-009](../open-items.md#oi-009). [E-029](../../evidence/evidence-ledger.md#e-029) [E-035](../../evidence/evidence-ledger.md#e-035) |
| Pricing, onboarding, renewal, and expansion | `[Verified source/public alignment]` with `[unknown customer state]` | Starter/Growth/Business/Enterprise benefits, usage rules, grace, and upgrade paths describe what customers buy and when access can lock. | Central gates and current v5 benefits broadly align, but multiple plan generations, Paddle-fetched prices, custom Enterprise terms, grandfathering, CE/EE paths, and tracker variants prevent one public page from establishing a tenant's contract. | A quote, onboarding, upgrade, or renewal can present the wrong capability, limit, price, or access outcome. | Product/billing authority, customer-contract owner, support exception owner, and test owner are unknown. | Produce the versioned effective entitlement matrix and representative tenant results under [OI-009](../open-items.md#oi-009). [E-025](../../evidence/evidence-ledger.md#e-025) [E-033](../../evidence/evidence-ledger.md#e-033) |
| Integration demo and customer delivery | `[Verified contract mismatch]` | Events API documentation presents `202` acceptance and a `{}` success example. | Pinned source and repository checks return text `ok`; GitHub issue #1246 and PR #2351 show that response history. A `202` can also represent a policy-dropped event and does not prove durable ClickHouse insertion. No live client journey was observed. | An integration can parse the wrong body or treat acceptance as durable analytics, producing false success, retry errors, or trust loss. | API contract owner, documentation approver, ingestion SLO owner, and customer-impact owner are unknown. | Align the deployed response contract under [OI-012](../open-items.md#oi-012), prove durability under [OI-001](../open-items.md#oi-001), and demonstrate the full path under [OI-008](../open-items.md#oi-008). [E-002](../../evidence/evidence-ledger.md#e-002) [E-021](../../evidence/evidence-ledger.md#e-021) [E-032](../../evidence/evidence-ledger.md#e-032) |
| Privacy-led trust and assurance | `[Plausible public claim]` plus `[verified source conflict]` | Public policy says raw IP/User-Agent are not stored and the visitor-identifier salt is deleted every 24 hours. | Pinned source retains current/previous salts and deletes rows older than 48 hours. Separately, source conditionally adds an ingestion request containing raw IP/User-Agent to Sentry context while its filter changes only the fingerprint. Actual Cloud DSN use, error occurrence, vendor receipt/retention, lifecycle semantics, and customer-supplied field classification remain unknown. | Repeating the categorical privacy story without reconciliation can undermine sales assurance and customer trust; changing salt behavior prematurely can also break intended cross-midnight session continuity. | Privacy/legal approver, data owner, observability owner, implementation owner, and claim publisher are unknown. | Remove/reconcile the conditional Sentry disclosure under [OI-015](../open-items.md#oi-015) and reconcile salt/data-lifecycle semantics under [OI-011](../open-items.md#oi-011); do not infer noncompliance or actual disclosure. [E-027](../../evidence/evidence-ledger.md#e-027) [E-031](../../evidence/evidence-ledger.md#e-031) [E-037](../../evidence/evidence-ledger.md#e-037) |
| Cloud onboarding, renewal, and trust | `[Plausible public claim]` with `[verified responsibility boundary]` | Managed Cloud is positioned as owning availability, backup, security, maintenance, capacity, monitoring, and frequent releases; the cutoff security page claimed remote backups and recovery procedures. | Repository configuration shows health, telemetry, queue, build, and migration primitives. Public incident history includes a November 2025 update that ingestion resumed while lost data was being restored. No completed restoration, RPO/RTO, alert-to-response, Cloud promotion, rollback, or control-effectiveness record was available. | A demo or renewal can appear healthy while recovery, loss reconciliation, or support assurance remains unproved; the CTO could inherit claims without the access to substantiate them. | Operations, incident, recovery, support, claim, and executive-risk owners are unknown. | Prove backup/recovery under [OI-021](../open-items.md#oi-021), detection-to-closure under [OI-023](../open-items.md#oi-023), and commit-to-runtime control under [OI-003](../open-items.md#oi-003). [E-046](../../evidence/evidence-ledger.md#e-046) [E-047](../../evidence/evidence-ledger.md#e-047) [E-048](../../evidence/evidence-ledger.md#e-048) [E-050](../../evidence/evidence-ledger.md#e-050) |
| CE onboarding and trust | `[Verified source/history finding]` with `[unknown incidence]` | Community Edition supports historical imports and is positioned as operator-managed software. | At the pinned commit, a failure-classification path can purge completed imported analytics; issue #6515 reports the outcome and PR #6547 proposed a scoped fix but remained open and unreviewed at the cutoff. Deployed versions and affected users are unknown. | A destructive import path can cause data loss and materially damage onboarding, retention, and open-source trust even when frequency and actual affected users are unknown. | Fix/release owner, advisory owner, support owner, and installed-version owner are unknown. | Correct and verify affected releases under [OI-006](../open-items.md#oi-006); do not infer incident count from the issue. [E-016](../../evidence/evidence-ledger.md#e-016) [E-028](../../evidence/evidence-ledger.md#e-028) |
| Data portability and offboarding | `[Verified source/public alignment]` with `[unknown operation]` | Customers can request quick aggregate exports and a broader queued native export with documented exclusions. | Source includes queued S3/local export workers, retries, notifications, object retrieval, and deletion, but no approved run established authorization, content correctness, completion, expiry, or failure recovery. | Onboarding assurance, customer review, or offboarding can depend on portability that is implemented but not demonstrated end to end. | Export owner, storage/security owner, support owner, and acceptance owner are unknown. | Exercise one authorized lifecycle under [OI-014](../open-items.md#oi-014). [E-026](../../evidence/evidence-ledger.md#e-026) [E-051](../../evidence/evidence-ledger.md#e-051) |
| Enterprise access-control demo | `[Verified source/public alignment]` with `[unknown tenant behavior]` | Enterprise SSO, JIT, session policy, roles, and shared-link controls are documented and source-visible. | Defaults and gates align, including owner recovery, but no safe tenant/IdP negative-path test or specialist review was available. | A sales or onboarding demo cannot responsibly stand in for tenant isolation, recovery, or customer-safe access behavior. | Identity/security owner, product authority, support/recovery owner, and demo owner are unknown. | Demonstrate tenant-effective access paths under [OI-013](../open-items.md#oi-013) and the full product journey under [OI-008](../open-items.md#oi-008). [E-024](../../evidence/evidence-ledger.md#e-024) |

## Commercial-Stage Consequences

| Stage | What the public corpus supports | What it does not support |
|---|---|---|
| Demo | A broad, coherent source-visible tracker, dashboard, query, goals, collaboration, SSO, import/export, and plan surface. | A claim that a current customer journey, tenant entitlement, integration response, data durability, SSO negative path, or export succeeds. No golden-path observation was authorized. |
| Onboarding | Detailed guides, central gates, edition boundaries, and explicit product constraints. | Customer-specific configuration, successful setup, current billing, Cloud/CE release adoption, support response, or absence of destructive import behavior. |
| Renewal | Public terms and product limits define a general service boundary; public status history demonstrates disclosure of interruptions. | Customer-specific obligation, satisfaction, loss reconciliation, SLA attainment, support outcome, or renewal probability. |
| Expansion | Source-visible Business/Enterprise gates and SSO/advanced-analysis support. | Fulfillment and acceptance of scheduled raw export, custom limits/retention, managed proxy, or any negotiated Enterprise commitment. |
| Trust and delivery | Public privacy/security/continuity statements and source-visible technical primitives. | Independent assurance, live controls, completed restoration, deployed claim version, customer harm, or regulatory compliance. |

## Material Unknowns And Closure Routes

- Golden-path consequence: because the [audit brief](../../audit-brief.md)
  approves no identity, fixture, or safe environment, this review cannot call
  the product demo-ready or demo-unready.
  [OI-008](../open-items.md#oi-008) owns the smallest authorized observation
  route.
- Vendor/commercial packet: no approved vendor agreement, customer contract,
  order form, renewal record, entitlement record, support commitment, or
  commercial ownership record was available in the
  [approved boundary](../../audit-brief.md). The shared
  `vendor-ownership-commercial` packet was therefore not requested; public
  terms and source references cannot populate those fields. Obtain the
  customer-effective commercial evidence through
  [OI-009](../open-items.md#oi-009) and the critical-service/vendor custody
  evidence through [OI-022](../open-items.md#oi-022).
- `Documented outside audited scope; not independently verified.` This applies
  to the separate Community Edition packaging/upgrade repository, any internal
  raw-export or managed-proxy service, private Cloud control records, customer
  contracts, Paddle/customer records, and support/renewal records.
- No amount, probability, contract breach, customer impact, financial-health
  conclusion, or individual performance conclusion is supported by this
  register.
