# PDR-001: Self-Hosted Short Links As Code

- Status: observed
- Evidence cutoff: July 22, 2026

## Decision Statement

vanityURLs lets an operator store exact and splat short links in Git, compile them into a read-only registry, and serve redirects from a Cloudflare Worker on the operator’s short domain.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Product behavior/promise | Branded, source-controlled short links on an operator-owned domain. | `README.md`; website setup and link-format docs | No adoption or user-satisfaction evidence. |
| Implementation | Build/registry/Worker source supports exact tree lookup and splat remainder substitution. | `scripts/build.mjs`; `scripts/lib/runtime-registry.mjs`; `scripts/workers/worker.mjs` | No build or request executed. |
| Runtime/demonstration | `v8s-link` contains instance configuration and is described as the official demo. | `v8s-link` source; website docs | Live demo behavior through cutoff was not observed. |
| Approval/specialist sign-off | Durable source and public releases exist. | [E-009](../../../evidence/evidence-ledger.md) | No formal product owner/customer acceptance. |

## Constraints, Options, And Tradeoffs

Git history provides reviewability and portability but link changes are deploy-time rather than instantly mutable through an admin API. Cloudflare and a short domain are required external dependencies.

## Impacts And Boundaries

The core value is reproducible and forkable. Continuity of an existing public domain and community identity remains an operational/ownership question, not a product-code feature.

## Change, Reversal, And Follow-Up

Adding a mutable link API would change security, identity, data, recovery, and cost. Validate the current golden path with OI-004 before expanding scope.
