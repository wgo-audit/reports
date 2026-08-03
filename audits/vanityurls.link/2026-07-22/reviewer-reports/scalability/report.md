# Scalability

## Audit Question, Depth, And Evidence Boundary

This detailed review asks whether vanityURLs supports a realistic growth envelope across requests, link/configuration data, build/maintenance work, providers, operations, degradation, and cost. It uses cutoff-pinned Worker/build/check/Terraform/Wrangler source, the Architecture/Product/Code Quality/Security handoffs, and recovery documentation through July 22, 2026. No production metrics, plan/quota data, logs, registry artifact, benchmark, load test, live request, alert, cost, or recovery exercise was available.

## Coverage And Material Gaps

Coverage includes public request resolution, registry loading/tree lookup, link/schedule/policy growth, protected operations/JWKS, analytics, edge rate limiting, target checks, failure behavior, and provider dependence. The design is stateless and database-free, which reduces scaling complexity. The material gap is a complete absence of measured workload and provider envelope: no request/latency/error baseline, registry-size budget, build duration, Cloudflare quota/plan, analytics quota, availability target, or alert/rollback threshold.

## Key Findings

| Finding | Evidence links | Confidence and limitation | Consequence |
|---|---|---|---|
| The runtime has a favorable scaling shape: stateless Worker, no application database/queue, read-only generated registry, and tree traversal by path segments. | [Capacity view](../../controls/scalability/capacity-and-degradation.md), [ADR-003](../../controls/architecture/adr/ADR-003-cloudflare-worker-runtime.md) | High for source topology; no measured latency/capacity. | A third party avoids operating stateful infrastructure, but Cloudflare/assets limits become the operating envelope. |
| Every redirect depends on a readable generated registry asset; no repository-defined last-known-good runtime fallback exists. | Worker `loadRegistry`; [capacity view](../../controls/scalability/capacity-and-degradation.md) | High for source behavior; platform asset caching/rollback unknown. | Registry/build/deploy failure can affect the entire redirect service; recovery relies on external deployment rollback. |
| Link, schedule, policy, language, and page growth is processed in build/check tooling with no declared size/time budget. | Build/registry/check source; [Code Quality matrix](../../controls/quality/change-safety-matrix.md) | High for implementation; no representative large fixture or benchmark. | Maintainability and deployment time may become the first growth constraint before request serving does. |
| Optional analytics degrades safely for redirect latency because sends are asynchronous and failures are caught, but events have no retry/queue and provider quotas are unknown. | Analytics source/docs; [PDR-007](../../controls/product/pdr/PDR-007-private-operations-and-optional-analytics.md) | High source intent; live event delivery unobserved. | Baseline operation can avoid this dependency; enabled analytics trades resilience for lossy best-effort observability. |
| Source declares a fixed per-IP candidate-request rate limit for the demo, but applied state, plan limits, and false-positive behavior are unknown. | `v8s-config/main.tf`; network-protection docs; [Security edge view](../../controls/security/diagrams/edge-exposure-view.md) | High for intended configuration; live rule/traffic absent. | Shared-IP/high-volume legitimate users may degrade, while absent controls may expose Worker/analytics quotas. |
| Access key caching and stale-key fallback limit private-path dependence on the cert endpoint, while missing/unusable identity configuration fails private paths closed. | Worker source/tests; [E-014](../../evidence/evidence-ledger.md) | High for source behavior; no real rotation/outage exercise. | Public redirects can remain available while operations visibility becomes unavailable—an important incident response asymmetry. |

### Decision Insights

- **Keep the product stateless until measured evidence requires more infrastructure.** Current architecture is simple and portable; adding a database/queue would expand takeover, security, recovery, and cost burden. Smallest proof before change: OI-011 with realistic registry/request envelopes.
- **Define capacity around the whole operator path, not only request throughput.** Build, target validation, deploy size/time, registry availability, provider quotas, and alert/rollback can fail before Worker compute. Smallest action: include all dimensions in OI-011.
- **Use analytics-disabled as the continuity baseline.** It preserves redirect service and removes unbounded provider quota/cost/retention dependencies. Enable only with owned limits and loss tolerance.

## Selected Outputs

The material workload, data-growth, provider, and degradation questions triggered [capacity and degradation envelope](../../controls/scalability/capacity-and-degradation.md), including an explicit source-bounded failure sequence.

## Material Omissions, Unknowns, And Stakeholder Questions

- Current/expected request rate, burst, latency, error, registry size/link count, build duration, target-check duration, deploy size, availability objective, and recovery time: OI-011.
- Current Cloudflare/Access/Workers/assets/DNS/rate-limit/analytics plan and quotas: OI-011 with Expense Exposure input.
- Applied edge controls, alert routing, last-known-good deployment, and recovery performance: OI-006.
- Whether registry or Access/analytics degradation has occurred in practice: no public incident/metric record.

## Reconciliation

Source simplicity was reconciled as a favorable architecture characteristic, not capacity proof. The fixed Terraform rate limit is treated as demo-instance intent, not a universal product maximum or applied live rule. Analytics documentation correctly states provider limits are account-specific; the absence of those facts prevents an enabled-analytics envelope.

## Bounded Conclusion And Downstream Guidance

vanityURLs is architecturally capable of scaling simply for a small-to-moderate redirect service, and its stateless design is a strong third-party-operability advantage. No evidence supports a numeric or production-ready capacity claim. Business Continuity may use degradation paths; Expense Exposure must obtain plan/quota/cost facts; Revenue Risk may use the absence of service-level evidence. None may claim a bottleneck, capacity, availability, or provider sufficiency from source alone.
