# Product Manager Notes

## Capability, Workflow, And Promise Position

The visible product is coherent: a configurable tracker and Events API feed a shared statistics/query layer used by the dashboard and public APIs; goals, revenue, funnels, journeys, roles, shared links, SSO, imports, aggregate exports, native exports, plans, and edition gates are represented in source. Public documentation generally names important constraints such as import limitations, output warnings, API limits, usage grace, SSO owner recovery, and Cloud-versus-CE responsibilities. The detailed mapping is in the [capability contract matrix](controls/product/capability-contract-matrix.md) and [rules/output semantics](controls/product/rules-and-output-semantics.md).

This is strong evidence of product rigor and concern for users. Public promises generally map to implementation, limitations are usually stated rather than hidden, and issues/PRs show concrete user problems entering the engineering process. The gaps below are bounded promise or acceptance questions; they do not outweigh the overall positive product signal.

Four promise boundaries need product ownership rather than purely technical fixes:

- Events API `202` means accepted into the path, not confirmed durable analytics. Policy-dropped events can also return `202`, and public `{}` response documentation conflicts with source/tests using `ok` ([OI-001](controls/open-items.md#oi-001), [OI-012](controls/open-items.md#oi-012)).
- Public plan copy broadly aligns with v5 gates, but multiple generations, grandfathering, custom Enterprise terms, Paddle-fetched prices, CE/EE profiles, and tracker variants mean no public page is the customer-effective source of truth ([OI-009](controls/open-items.md#oi-009)).
- Scheduled raw-event export is a specific Enterprise promise, but the implementing delivery service, schema, security, SLO, and one completed customer delivery were not established in the approved monorepo ([OI-010](controls/open-items.md#oi-010)). This may exist privately; its absence from the audit is not evidence of product absence.
- Privacy differentiation is materially qualified by the 24h-versus-48h salt wording and conditional Sentry request context ([OI-011](controls/open-items.md#oi-011), [OI-015](controls/open-items.md#oi-015)). Product copy should not be repeated categorically until engineering facts and qualified legal scope reconcile.

The audit could not classify the product as demo-ready or demo-unready because no safe identity, fixture, or environment was approved. Source-visible breadth and tests are not a current customer journey. One authorized tracker-to-ingestion-to-dashboard journey, tier negatives, SSO negatives, native export, and customer-effective entitlements belong in the first-month verification baseline ([OI-008](controls/open-items.md#oi-008), [OI-013](controls/open-items.md#oi-013), [OI-014](controls/open-items.md#oi-014)).

## Decisions And Specialist Sign-Off Boundaries

- Product, ingestion, security, support, and operations must decide the accepted unauthenticated-ingestion abuse model after measuring spoofing, drops, false positives, affected tenants, and cost ([OI-016](controls/open-items.md#oi-016)).
- Product/billing/support must own one versioned entitlement matrix reconciled to contracts, billing, runtime gates, documentation, supported releases, and representative current/grandfathered tenants ([OI-009](controls/open-items.md#oi-009)).
- Enterprise product/data/security/support must demonstrate scheduled raw delivery or narrow/reword the promise ([OI-010](controls/open-items.md#oi-010)).
- Privacy/legal specialists must approve visitor-identity, consent, location, deletion, breach, subprocessor, and data-classification wording. A provider-hosted legal assessment is attributed analysis, not certification, and its 24-hour premise conflicts with visible source ([OI-028](controls/open-items.md#oi-028)).
- Cloud, recovery, scan, and security claims require the relevant technical owner evidence before product or marketing approval. Current August 2026 page expansions cannot backfill the cutoff version.

## Material Gaps, Risks, And Next Work

| Priority | Product/business exposure | Required product action | Technical/specialist dependency |
|---|---|---|---|
| Immediate | CE historical imports can be purged after cleanup-worker failure | Stop/fix the path; identify affected releases; coordinate recovery and operator communication | [OI-006](controls/open-items.md#oi-006) |
| Immediate | Privacy copy may outrun Sentry and salt behavior | Pause categorical reuse where necessary; establish claim owner/version; support correction | [OI-011](controls/open-items.md#oi-011), [OI-015](controls/open-items.md#oi-015), [OI-028](controls/open-items.md#oi-028) |
| Onboarding discovery | Cloud reliability/recovery operation is private and therefore not publicly verifiable | Learn the operating model and ensure customer wording maps to its scope and owners | [OI-003](controls/open-items.md#oi-003), [OI-021](controls/open-items.md#oi-021)–[OI-024](controls/open-items.md#oi-024) |
| High | Enterprise raw export may have an invisible service/operating boundary | Produce service, runbook, entitlement, security and customer-acceptance evidence | [OI-010](controls/open-items.md#oi-010) |
| High | Effective paid product can vary by plan generation, contract, edition and tenant | Create the capability/entitlement source of truth and change-reconciliation owner | [OI-009](controls/open-items.md#oi-009) |
| Medium | Events API response and durability semantics can produce false success or client incompatibility | Version and document the response/acceptance contract | [OI-001](controls/open-items.md#oi-001), [OI-012](controls/open-items.md#oi-012) |
| Medium | Native export and tenant/SSO behavior are implemented but not demonstrated | Run safe end-to-end acceptance/negative cases | [OI-013](controls/open-items.md#oi-013), [OI-014](controls/open-items.md#oi-014) |
| Onboarding discovery | Scale/cost and custom terms are private management information | Build the normal SLO, demand, cost-to-serve and contract baseline before major roadmap or pricing changes | [OI-025](controls/open-items.md#oi-025), [OI-027](controls/open-items.md#oi-027) |

The commercial-stage consequence register is in [Claim Governance](controls/revenue/claim-governance-and-exposure-register.md). It deliberately does not infer revenue, churn, customer harm, renewal likelihood, or financial health.

## Evidence And Limits

This note separates source facts, Plausible public claims, bounded inferences, and unknowns. Merged code and green CI do not prove deployment or customer acceptance, but they are still affirmative evidence of disciplined product development. Public issue reports establish attributed reports, not incidence. No customer contracts, tenant records, billing data, support outcomes, usage analytics, or live product demonstration were available; that normal confidentiality is neutral and does not reduce the overall product assessment. The separate Community Edition packaging/upgrade and customer-documentation repositories were outside the approved source corpus and are not independently verified here.

For the role decision and detailed evidence-derived questions, use the [Executive Summary](executive-summary.md). For implementation constraints, use [Technical Lead Notes](technical-lead-notes.md).

Audit execution cost is reported separately: [API-Equivalent Cost Estimate](controls/cost-estimate.md). Its **$109.29 USD** total is a reproducible API-equivalent estimate, not a Codex invoice or a Plausible operating-cost conclusion.
