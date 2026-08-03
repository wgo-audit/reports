# ADR-004: Layered Edge And Operational Access Controls

- Status: observed
- Evidence cutoff: July 22, 2026

## Decision Statement

vanityURLs separates public redirect behavior, Worker-side validation/blocking, protected operational pages, and Cloudflare account/zone controls into layered trust boundaries.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Implementation | Worker source validates paths/targets and fails closed for protected pages; Terraform declares Access, WAF, redirects, and rate limits. | Worker source; `v8s-config/main.tf`; [recovery packet](../../../evidence/packets/recovery-and-operations.md) | Terraform state/application and runtime execution are unknown. |
| Runtime/live state | Instance configuration names an Access team domain and disables optional analytics. | `v8s-link/wrangler.toml` | Audience secret, effective policies, WAF events, and live analytics are unknown. |
| Rationale | Keep ordinary redirects open while restricting operational views and filtering abuse at the edge. | Website access, network-protection, runtime-security docs | No approved threat exercise or operator validation. |
| Approval | Source/configuration and documentation are aligned on intended layers. | [E-004/E-007](../../../evidence/evidence-ledger.md) | Current control owner and approval authority are unknown. |

## Constraints, Options, And Tradeoffs

Layering reduces dependence on a single code check, but Cloudflare configuration can drift from Git and requires external administrative access. Overbroad edge rules can block legitimate short-link traffic.

## Impacts And Boundaries

Security must distinguish source behavior from applied controls. A successor needs access to both Git and Cloudflare; code ownership alone cannot operate or recover the current protected surfaces.

## Change, Reversal, And Follow-Up

Close OI-006 with redacted live-state comparison, role ownership, drift review, and safe operator validation. Do not store secret values in audit artifacts.
