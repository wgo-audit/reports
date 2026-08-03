# PDR-007: Private Operations And Optional Analytics

- Status: observed
- Evidence cutoff: July 22, 2026

## Decision Statement

Statistics and test surfaces are private behind Cloudflare Access; raw runtime data stays non-public; analytics is disabled by default and, when configured, emits provider events asynchronously so redirect responses do not wait for analytics.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Product behavior/promise | A working production redirector without analytics is valid; the product does not phone home. | Analytics docs; instance README | No privacy/customer acceptance evidence. |
| Implementation | Worker enforces protected paths/raw-file guards and uses `ctx.waitUntil()` for optional providers; instance declares analytics disabled. | Worker source; `v8s-link/wrangler.toml`; Access Terraform | Live controls/provider behavior unknown. |
| Runtime/demonstration | Public docs instruct signed-out Access and analytics smoke checks. | Quickstart/analytics docs | Neither check was observed. |
| Approval/specialist sign-off | Source and docs align on opt-in behavior. | [E-014/E-015](../../../evidence/evidence-ledger.md) | No privacy or security specialist sign-off; Access ownership unknown. |

## Constraints, Options, And Tradeoffs

Optional analytics minimizes baseline data sharing, while enabled providers create separate credentials, quotas, retention, and privacy obligations. Private pages depend on correctly configured Access.

## Impacts And Boundaries

Independent operation is possible with analytics disabled, reducing handover scope. Existing private operational visibility still requires external identity and account transfer.

## Change, Reversal, And Follow-Up

Do not make analytics mandatory without a new privacy/product decision. Validate Access fail-closed behavior and provider-failure isolation during an approved operator exercise.
