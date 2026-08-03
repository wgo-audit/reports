# Burn, Renewal, And Interruption Register

## Evidence Boundary

No invoice, billing console, contract, donation, budget, usage statement, labor rate, tax record, renewal notice, vendor plan attachment, or payment method was approved. Every monetary amount is therefore `unknown`. A named dependency is not evidence of spend. This register tracks interruption and verification needs, not estimated cost.

## Exposure Register

| Surface | Public dependency evidence | Amount/period | Renewal/plan/term | Payment and accountable owner | Interruption consequence | Closure evidence |
|---|---|---|---|---|---|---|
| Short domain/registrar | Registered short domain is a setup prerequisite; `v8s.link` is the public demo identity | `unknown` | Registrar, expiry, auto-renew, transfer lock, term `unknown` | `unknown` | Existing links and community trust can fail even when code survives | OI-013: redacted registrar, expiry/renewal, two recipients, payment backup, transfer/recovery proof |
| Cloudflare DNS/Workers/assets | Required product platform and current source target | `unknown` | Attached plan, quotas, overages, support, term `unknown`; docs describe a Free-plan baseline but not live entitlement | `unknown` | DNS/TLS/redirect service can stop or become unchangeable | OI-006/OI-013: redacted plan/quota/billing owner and continuity evidence |
| Cloudflare Access/WAF/rate limits/logs | Significant security/operations controls declared | `unknown` | Available features/limits depend on current plan; live entitlement `unknown` | `unknown` | Private operations, abuse protection, or alert visibility can degrade | OI-006/OI-011/OI-013 |
| GitHub | Four public repositories, Actions, releases, collaboration identity | `unknown` | Account/org plan, Actions quota, support, billing/term `unknown` | `unknown` | Canonical source/release/change path can be interrupted; source can be mirrored | OI-002/OI-013 |
| Website hosting/build | Cloudflare Worker/static assets plus external build toolchain declarations | `unknown` | Plan/quota/renewal `unknown` | `unknown` | Operator source of truth may be unavailable or stale | OI-008/OI-013 |
| Analytics providers | Optional Umami/Fathom; reference instance source disables analytics | `unknown` | Provider account/plan/retention/term `unknown` | `unknown` | Metrics can be lost; redirects should continue | Keep disabled for successor baseline; verify only if enabled |
| Maintainer/contributor labor | Public docs say support is volunteer/best-effort | `unknown` | Availability/commitment/rates `unknown` | No company or staffing budget evidenced | Work can stall; no financial liability is established | OI-004 captures effort; do not monetize without approved rates |
| Recovery/security incident | Missing alerts/recovery can prolong interruption | `unknown` | No insurance, reserve, SLA, incident vendor, or liability evidence | `unknown` | Community distrust and operational work, amount unbounded | OI-012 plus any later approved cost evidence |

## Bounded Conclusion

Cash burn and liabilities cannot be calculated. Interruption exposure is material because domain and platform renewals/ownership are unknown and can stop the existing service. Optional analytics is the clearest removable exposure. The smallest safe action is OI-013, not a speculative cost estimate.
