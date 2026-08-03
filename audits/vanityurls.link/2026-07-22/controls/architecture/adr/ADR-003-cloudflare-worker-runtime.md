# ADR-003: Cloudflare Worker Runtime

- Status: observed
- Evidence cutoff: July 22, 2026

## Decision Statement

The product compiles human-authored link/configuration files and public assets into a Cloudflare Worker deployment whose request handler resolves a read-only registry and delegates static files to an assets binding.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Implementation | Build scripts generate the registry and Worker source; Wrangler declares `main`, assets, custom-domain routing, and Worker-first patterns. | `scripts/build.mjs`; `scripts/lib/runtime-registry.mjs`; `scripts/workers/worker.mjs`; `wrangler.toml` | No local build or request was run. |
| Runtime/live state | Invocation logging is declared and preview/`workers.dev` surfaces are disabled. | Product and instance `wrangler.toml` | No live Worker, logs, DNS, or response was observed. |
| Rationale | A source-controlled, low-state redirector avoids a mutable application database and authenticated edit API. | Website security model; source ADR 0013 | Performance and availability rationale is not independently demonstrated. |
| Approval | Durable implementation and documentation exist. | [E-004](../../../evidence/evidence-ledger.md) | Live acceptance and account authority are unknown. |

## Constraints, Options, And Tradeoffs

The runtime is operationally simple and limits mutable data risk. Changes require build/deploy cycles, and availability inherits Cloudflare, DNS, domain, and repository deployment dependencies.

## Impacts And Boundaries

Public redirects can be independently recreated from Git. Existing-domain continuity still depends on registrar, DNS, Cloudflare, and deployment control outside source.

## Change, Reversal, And Follow-Up

Adding mutable storage, queues, or an administrative API would materially change security, recovery, privacy, and operating cost. Require new Architecture and Product records before doing so.
