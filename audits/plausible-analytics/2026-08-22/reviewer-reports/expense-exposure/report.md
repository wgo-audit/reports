# Expense Exposure

## Audit Question, Depth, And Evidence Boundary

This detailed reviewer asked what actual or potential cash exposure comes from infrastructure, software, staffing, commitments, and failure modes as of 2026-08-22 22:08:28 EDT. It inspected the pinned public monorepo, cutoff-valid public customer terms and subscription/Cloud-versus-CE claims, public status history, and specific merged resource-control PRs #4839, #6018, and #6591. Public source establishes technical and customer-delivery surfaces; it does not establish that a dependency is enabled or paid.

The approved boundary excludes production/cloud accounts, bills, contracts, vendor portals, usage/capacity metrics, customer mix, margins, payroll, staffing plans, and approval records. No spend, runway, profitability, individual performance, or financial health is inferred.

## Coverage And Material Gaps

Coverage included PostgreSQL/ClickHouse/Oban ingestion and query paths; native and scheduled export boundaries; plan/usage/grace behavior; Paddle price/subscription/invoice calls; configured infrastructure, monitoring, CDN, storage, support, email, geolocation, registry and delivery services; public provider incidents; and source-visible sampling, timeout, retry, and deletion limits. [E-057–E-061](../../evidence/evidence-ledger.md#e-057) are the reviewer-owned evidence.

The material gap is the complete actual-cost and commitment baseline in [OI-025](../../controls/open-items.md#oi-025). The conditional expense view was triggered by provider-interruption evidence with potential business consequence and source-visible payment/customer-delivery dependencies. A `vendor-ownership-commercial` packet was not requested because no approved billing, usage, contract, renewal, or vendor-control record existed for a collector to inspect. Business Continuity owns recovery and successor control; Scalability owns the capacity model.

## Key Findings

| Finding | Severity | Effort | Evidence links | Confidence and limitation | Consequence | Taxonomy |
|---|---|---|---|---|---|---|
| Actual infrastructure, software, staffing, vendor, commitment, renewal, quota, and cost-to-serve exposure cannot be bounded from the approved public corpus. | High | M | [E-057](../../evidence/evidence-ledger.md#e-057), [E-058](../../evidence/evidence-ledger.md#e-058), [E-059](../../evidence/evidence-ledger.md#e-059), [OI-025](../../controls/open-items.md#oi-025) | High confidence that the approved corpus has no such records; underlying amounts and financial materiality are unknown. | Accepting budget and vendor accountability without the redacted expense/usage/term packet could transfer obligations or concentration that the candidate cannot size or control. | none |
| Public customer terms can let consumption precede price correction: occasional spikes are not charged, collection continues while dashboards are locked, and custom Enterprise terms can raise volume, retention, API, proxy, and export obligations. | Medium | M | [E-025](../../evidence/evidence-ledger.md#e-025), [E-059](../../evidence/evidence-ledger.md#e-059), [OI-009](../../controls/open-items.md#oi-009), [OI-025](../../controls/open-items.md#oi-025) | Public promise and source controls are strong; customer mix, actual entitlements, price, cost allocation, and margin are unknown. The cost/revenue relationship is a reasoned inference. | Underpriced or unusually demanding tenants could create unrecognized compute, storage, egress, support, or bespoke-delivery burden. | none |
| Native analytics export deliberately uses a ClickHouse connection without the ordinary query-execution limit, inside a 15-minute worker with up to three attempts; source separately avoids repeating successful work because it is costly. | Medium | S | [E-057](../../evidence/evidence-ledger.md#e-057), [OI-014](../../controls/open-items.md#oi-014), [OI-025](../../controls/open-items.md#oi-025) | High confidence in source; no queue history, archive size, retry rate, concurrency, unit cost, or live cancellation behavior. | Large or repeated exports can become a tenant-skewed compute, storage and egress exposure before the broader cost model exists. | none |
| Paddle is source-visible in price, subscription-change, invoice, and subscription-state paths, while public terms assign it payment and returns; a price-fetch failure has a bounded fallback, but commercial and operational concentration is unknown. | Medium | S | [E-058](../../evidence/evidence-ledger.md#e-058), [OI-022](../../controls/open-items.md#oi-022), [OI-025](../../controls/open-items.md#oi-025) | Strong source/claim confidence; no fee, SLA, incident, reconciliation, account owner, term, or fallback exercise. | Provider or account interruption can degrade pricing, upgrades, invoices, payment operations, or support even if existing local subscription state remains. | none |
| Public status history proves infrastructure-provider interruption can reach the service, but its cash, credit, support, churn, recovery-labor, and contract consequences are not public. | Medium | M | [E-050](../../evidence/evidence-ledger.md#e-050), [OI-021](../../controls/open-items.md#oi-021), [OI-022](../../controls/open-items.md#oi-022), [OI-025](../../controls/open-items.md#oi-025) | Incident occurrence and stated restoration are public; completeness, provider identity, duration/cost allocation, SLA and customer impact are unavailable. | A provider dependency can create simultaneous availability, recovery, support, and commercial exposure; magnitude must be proved, not assumed. | none |

## Mandate-Relevant Strengths

- Merged PRs #4839, #6018, and #6591 retain source-visible sampling, query-time, partition, and concurrency bounds for expensive ClickHouse work ([E-060](../../evidence/evidence-ledger.md#e-060)).
- Export work has explicit attempt and worker-time bounds, and notification delivery is separated specifically to avoid repeating an already successful export ([E-057](../../evidence/evidence-ledger.md#e-057)).
- Versioned plans, centralized quota checks, grace/lock behavior, and Paddle failure handling make material billing and usage decision points discoverable in source ([E-025](../../evidence/evidence-ledger.md#e-025), [E-058](../../evidence/evidence-ledger.md#e-058)).

### Decision Insights

- **Normal onboarding baseline:** use [OI-025](../../controls/open-items.md#oi-025) to understand trailing-12-month expense, usage, contracts, budgets, renewal owners, quotas, and capacity guardrails after joining. These records are private by nature; their absence from public evidence supports no adverse cost, runway, or role-acceptance inference.
- **Pricing and Enterprise expansion sequence:** reconcile customer-effective entitlements, measured cost-to-serve, and scheduled-export delivery before raising retention, API, volume, proxy, or export commitments. Public terms deliberately absorb some spike/grace consumption and custom terms vary delivery; changing packaging before measuring that relationship can worsen an unknown margin. Smallest next proof: pair [OI-009](../../controls/open-items.md#oi-009) with [OI-025](../../controls/open-items.md#oi-025).
- **Capacity-change stop condition:** preserve or replace the current sampling, ordinary-query timeout, deletion-concurrency, and export-worker bounds only after production demand and accuracy/cost tradeoffs are measured. The source shows deliberate limits, but not realized savings or saturation. Smallest next proof: Scalability should build the capacity model using [E-057](../../evidence/evidence-ledger.md#e-057) and [E-060](../../evidence/evidence-ledger.md#e-060), without treating either as spend evidence.

## Selected Outputs

- Triggered conditional [burn, renewal, and vendor-control boundary](../../controls/expense/burn-and-renewal.md). It is a potential-exposure map, not a burn estimate.
- The required cost/interruption assessment is this report.

The vendor commercial packet was not produced because no approved source could populate it. [OI-025](../../controls/open-items.md#oi-025) is the closure route.

## Material Omissions, Unknowns, And Auditor Questions

Unknowns include all actual amounts; vendor/staffing mix; live utilization and capacity; price and unit economics; customer mix and entitlements; vendor accounts, fees, tiers, quotas, renewals, credits, taxes, SLAs, exits and owners; cost allocation; and provider-incident commercial consequences. These are proof needs, not questions answerable by auditor assertion, and are routed through [OI-025](../../controls/open-items.md#oi-025), [OI-022](../../controls/open-items.md#oi-022), and [OI-024](../../controls/open-items.md#oi-024). No mandate, priority, success-outcome, or authority question requiring a wave-boundary auditor answer was raised.

Seven of seven dependency-free source checks passed; zero failed, errored, or skipped. Application tests: 0 passed, 0 failed, 0 errors, 0 skipped because no application test was run and dependency installation/restoration was not authorized. No vendor API, billing access, load test, export, deployment, production operation, or secret access was attempted ([E-061](../../evidence/evidence-ledger.md#e-061)).

## Reconciliation

No material source conflict was found. Public customer terms describe what Plausible promises or charges customers; they are not evidence of Plausible's own vendor terms or margin. Source-visible dependencies were classified as potential exposure rather than spend. Provider incidents established interruption, not financial materiality. Exactly one bounded quality worker completed terminally; its feedback was applied in one revision to the selected expense view.

## Bounded Conclusion And Downstream Guidance

The reviewer establishes a source-bounded map of infrastructure, payment, export, monitoring, vendor, and provider-interruption exposure, plus visible resource safeguards. It does not establish burn, staffing cost, contracts, renewal risk, utilization, margin, runway, financial health, or any paid vendor's live materiality. The Expense Exposure reviewer is complete with open verification under [OI-025](../../controls/open-items.md#oi-025).

Scalability should reuse the PostgreSQL/ClickHouse/export and resource-bound evidence to identify capacity bottlenecks, but must not convert them into spend. Revenue Risk should reuse the customer promise and Paddle boundaries, but must not infer revenue or churn. Business Continuity remains authoritative for recovery, successor access, and provider-loss control.
